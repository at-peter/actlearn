'''
This is the script that will be used to create the gridworld environment: 

The code that is currently in here is the depricated code from RL2 project. 
It will be the basis for the new code. 
'''

# import numpy as np

# '''
# This is where I will be making the stochastic gridworld environement. 

# Environment mechanics: 
# - start position -- this could be hardcoded but may also be worth looking into the idea of having the starting positions also stochastic
# - goal position -- there will be many goals that are fairly easy to find, but they are not always there. They will stochastically happen. 


# '''
# current_state = None
# terminal_1 = None
# terminal_2 = None
# R_1 = None 
# R_2 = None

# def env_init():
#     global current_state, terminal_1,terminal_2
    
#     terminal_1 = [7,3]
#     terminal_2 = [9,9]
#     # terminal_1 = [9,9]
    
#     return

# def env_start():
#     # set the starting location, get the rewards 
#     global R_1, R_2 , current_state
#     start_state = [0,0]
#     R_1 = max(min(np.random.normal(4,1),0.1),0)
#     R_2 = max(min(np.random.normal(3, 2), 7), 0)
#     # R_1 = 1
#     current_state = start_state 
#     return start_state

# def env_step(action):
    
#     global current_state, R_1, R_2
#     new_state = [0,0]
#     the_state = current_state
#     # action logic should go here 
#     '''
#     Check if current state is at a wall
#         Walls are:
#         - top = [:,0]
#         - Right = [4,:]
#         - bottom = [:,4]
#         - Left = [0,:]
#     Perform action 
#     update state 
#     check if state is terminal 
#     get reward depending on if you are terminal or not. 
    
#     '''
#     # ACTION PHASE: 
#     if action == 0: 
#         # up
#         new_state[0] = the_state[0]
#         new_state[1] = the_state[1] - 1 
    
#     elif action == 1:
#         # right
#         new_state[0] = current_state[0] + 1 
#         new_state[1] = current_state[1] 
    
#     elif action == 2:
#         # down 
#         new_state[0] = current_state[0]
#         new_state[1] = current_state[1] + 1  
    
#     elif action == 3:
#         # left  
#         new_state[0] = current_state[0] - 1
#         new_state[1] = current_state[1] 
    
#     else: 
#         print('Not a valid action')

#     # WALL PHASE: 
    
#     if new_state[1] == -1:
#         new_state[1] = 0
#     elif new_state[0] == -1: 
#         new_state[0] = 0
#     elif new_state[1] == 10: 
#         new_state[1] = 9
#     elif new_state[0] == 10:
#         new_state[0] = 9
#     #TODO: check the corner cases. I may need to turn theses into consecutive if statements. 

#     #UPDATE PHASE: 
#     current_state = new_state 

#     #TERMINAL PHASE: 
#     if current_state == terminal_1:
#             r = R_1 
#             is_terminal = True
#     elif current_state == terminal_2:
#             r = R_2 
#             is_terminal = True
#     else: 
#         is_terminal = False
#         r = 0 

#     results = {'reward': r ,'state': current_state , 'isTerminal': is_terminal}
#     return results 

# def env_cleanup():

#     return 

# def env_message(in_message):
#     return ""

