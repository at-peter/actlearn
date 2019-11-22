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
        self.z = [0]*self.maxSize 
        self.iht = IHT(self.maxSize)
        self.weights = [0]*self.maxSize
        self.numTilings = 8 
        self.stepsize = 0.1/self.numTilings
        
        self._gamma = 0.05
        self._lambda = 0.2
        self._epsilon = 0.05 

        #
        
        self.last_state = [0,0]

    def _policy(self, p, v):
        '''
        This method perfomes the epsilon check and action selection based on the current state. 
        '''
        action = 0 
        estimate = 0
        '''
        action is between -1 and 1
        '''
        chance_of_random_action = np.random.random_sample()

        if chance_of_random_action <= self._epsilon:
            #take the random action 
            action = np.random.choice([-1,1])
        else:
            # query the estimate:
            tiles = self._tileEncode_decoder(p,v) 
            for tile in tiles:
                estimate += self.weights[tile]
            # act on policy: 
                action = estimate
        
        return action  
        
    def learn(self, environment, observations, reward):
        
        p = observations[0]
        v = observations[1]
        current_estimate = 0
        previous_estimate = 0
        # to change to sarsa lambda you simply need to include the previous action in the tile values 
        tiles = self._tileEncode_decoder(p, v)
        # tiles = self._tileEncode_decoder(p, v, a)
        previous_tiles = self._tileEncode_decoder(self.last_state[0],self.last_state[1])
        
        # Get the previous estimates: 
        previous_tiles = self._tileEncode_decoder(self.last_state[0], self.last_state[1])
        for tile in previous_tiles:
            previous_estimate += self.weights[tile]

         
        # Replacing Trace
        sf = self.stepsize
        self.z = [element * sf for element in self.z]
        for tile in tiles:
            current_estimate += self.weights[tile]
            self.z[tile] =  1 # not sure about how this should work..
        # update delta
        delt = reward + self._gamma*current_estimate - previous_estimate 
        #update weights 
        for tile in tiles: 
             self.weights[tile] += self.stepsize*self.z[tile]*delt
        #update state 
        self.last_state = observations
        return True

    def act(self, observations):
        '''
        This is the act method
        '''
        p = observations[0]
        v = observations[1]
        return self._policy(p, v) 

    def _tileEncode_decoder(self, p, v):
        '''
        This method scales the statespace onto a 10x10 grid
        '''
        v_scaleFactor = 10/(0.14)
        p_scaleFactor = 10/(1.8)
        return tiles(self.iht, self.numTilings, [p*p_scaleFactor,v*v_scaleFactor])
    
