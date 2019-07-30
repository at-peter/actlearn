class Trader:

    Q = None 
    prev_action = 0 
    prev_state = 0 
    alpha = None 
    gamma = None 

    def __init__(self, **kwargs): 
        '''
        This will take the place of agent init and agent start in GLue
        Things that need to be initialized: 
            - Actions
            - 
        '''

        return
   
    def Agent_learn(self, **kwargs):
        '''
        Agent_learn will have to keep track of 

        Agent learn will recieive obbservations 
        observations: {
            reward: int,
            grid_position: [x:int, y:int]
        }
        '''

        td_err = alpha*(reward + gamma* np.amax(Q[state[0], state[1], :]) - Q[prev_state[0],prev_state[1],prev_action])
        Q[prev_state[0], prev_state[1], prev_action] = Q[prev_state[0], prev_state[1], prev_action] + td_err


        td_err = self.alpha*()
        return 


    def Agent_act(self, **kwargs):
        '''
        act will take in observations and then produce an action based on the result 

        observations are: 
        {
            reward: int,
            grid_position: [x:int, y:int]

        }

        action will be int range(1,4) -> 

        elements that need to be 

        '''
    gen = random.randint(0, 100)
    if gen <= (epsilon*10): 
        # Random policy
        action = random.randint(0,3)
        
    else: 
        # MaxA Q Action selection 
        best_option = np.argwhere(Q[state[0],state[1],:] == np.amax(Q[state[0],state[1],:]))
        num_options = len(best_option)
        best_option = (random.choice(best_option))
        action = best_option[0]
        

        return action 