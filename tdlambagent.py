'''
This is the td lambda agent made in the act learn framework. 
'''

import numpy as np
from tiles3 import tiles, IHT

class agent:

    def __init__(self):
        '''
        This is the initialization of the agent class.
        '''
        self.maxSize = 65536
        # self.z = [0]*self.maxSize 
        self.z = np.zeros(self.maxSize)
        self.iht = IHT(self.maxSize)
        # self.weights = [0]*self.maxSize 
        # self.weights = np.random.uniform(-1.0,1.0,self.maxSize)
        self.weights = np.ones(self.maxSize)
        self.numTilings = 8 
        self.stepsize = 0.1/self.numTilings
        self._gamma = 0.9
        self._lambda = 0.2
        self._epsilon = 0.05 
        self._last_action = 0
        # action refactor
        self._current_action = 0 # this gets called and updated in agent._policy()
        self._previous_action = 0 # this gets called and updated in agent.learn()
        #
        self.last_state = [0,0]

    def _policy(self, p, v):
        '''
        This method performs the epsilon check and action selection based on the current state. 
        '''
        action = 0
        action_range = np.arange(-1, 1, 0.2)
        estimate = [-1.0]*len(action_range)
        estimate = np.array(estimate)
        action_index = 0
        '''
        action is between -1 and 1
        '''
        chance_of_random_action = np.random.random_sample()

        if chance_of_random_action <= self._epsilon:
            #take the random action 
            action = np.random.choice([-1,1])
            self._current_action = action
        else:
            # query the estimate:
            for i in range(len(action_range)):
                tiles = self._tileEncode_decoder(p,v,action_range[i]) 
                print("Policy",tiles)
                for tile in tiles:
                    estimate[i] += self.weights[tile]
            
            
            # act on policy: 
            
            action_index = np.argmax(estimate)
            action = action_range[action_index]    
            self._current_action = action
        
        
        return action  
        
    def learn(self, observations, reward):
        
        p = observations[0]
        v = observations[1]
        action_range = np.arange(-1, 1, 0.2)
        estimate =[0]*len(action_range)
        estimate = np.array(estimate)
        # current_estimate = 0
        # previous_estimate = 0
        # # to change to sarsa lambda you simply need to include the previous action in the tile values 
        # # tiles = self._tileEncode_decoder(p, v)
        # tiles = self._tileEncode_decoder(p, v, self._current_action)
        # previous_tiles = self._tileEncode_decoder(self.last_state[0],self.last_state[1], self._previous_action)
        
        # # Get the previous estimates: 
        # # previous_tiles = self._tileEncode_decoder(self.last_state[0], self.last_state[1])
        # for tile in previous_tiles:
        #     previous_estimate += self.weights[tile]

         
        # # Replacing Trace
        # sf = self.stepsize
        # self.z = [element * sf for element in self.z]
        # for tile in tiles:
        #     current_estimate += self.weights[tile]
        #     self.z[tile] =  1 # not sure about how this should work..
        # # update delta
        # delt = reward + self._gamma*current_estimate - previous_estimate 
        # #update weights 
        # for tile in tiles: 
        #      self.weights[tile] += self.stepsize*self.z[tile]*delt
        # #update state 
        # self.last_state = observations
        # self._previous_action = self._current_action
        
        # Section on previous action 
        delta = reward
        tiles = self._tileEncode_decoder(p,v, self._current_action)
        print('Learn, current action', tiles)
        for tile in tiles:
            delta = delta - self.weights[tile] # reward - estimate 
            self.z[tile] = 1 # replacing traces

        #sweep the next actions for the next best action: 
        # next_action = self._policy(p,v) # need to select the best action
        # Weight update 
        for i in range(len(action_range)):
            tiles = self._tileEncode_decoder(p,v,action_range[i]) 
            print('Action', i, 'tiles', tiles)
            for tile in tiles:
                estimate[i] = estimate[i] + self.weights[tile]
                 
            # act on policy: 
            # FIXME: Is the problem choice of action?
        action_index = np.argmax(estimate)
        print(action_index)
        action = action_range[action_index]    
        
        #weight update:
        tiles = self._tileEncode_decoder(p,v,action)
        print('Action selected:', action, 'Tiles', tiles)
        for tile in tiles:
            delta = delta + (self._gamma*self.weights[tile])
            #python array does not like me here 
            self.weights[tile] = self.weights[tile]*delta*self.z[tile]*self.stepsize
        
        #updates
        sf = self._gamma*self._lambda # scale factor 
        self.z = [element *sf for element in self.z] #update of z 
        self._previous_action = self._current_action
        self.last_state = observations
        return True


    def act(self, observations):
        '''
        This is the act method
        '''
        p = observations[0]
        v = observations[1]
        return self._policy(p, v) 

    def _tileEncode_decoder(self, p, v, action):
        '''
        This method scales the statespace onto a 10x10X10 grid
        '''
        v_scaleFactor = 10/(0.14)
        p_scaleFactor = 10/(1.8)
        action_scaleFactor = 10/2
        return tiles(self.iht, self.numTilings, [p*p_scaleFactor,v*v_scaleFactor, action*action_scaleFactor])
    
