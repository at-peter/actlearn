

# import gym 
# import numpy as np

#     class agent:

#         def __init__(self):
#             self.z = 0 
#             self._gamma = 0
#             self._lambda = 0
#             self.epsilon = 0.05 


#         def learn(self):
#             # update z

#             # update delta

#             #update weights 

#             #update state 

#         def act(self):
#             # choose action
            
#             val = np.random.randint(0,100)
        
#             if val < (self.epsilon*100):
#                 # select a random action. Gym features the option to not give a policy to the environment. in that event, the environment will select a random action for you :) 
#                 action = None
#             else: 
#                 #act according to the policy 
#                 # action selection will be the m
#                 action = 
            
#             return action 




from tiles3 import tiles, IHT

maxSize = 2048
iht = IHT(maxSize)
weights = [0]*maxSize
numTilings = 8
stepSize = 0.1/numTilings

def mytiles(p, v):
    '''
    This method scales the statespace onto a 10x10 grid
    '''
    v_scaleFactor = 10/(0.14)
    p_scaleFactor = 10/(1.8)
    return tiles(iht, numTilings, [p*p_scaleFactor,v*v_scaleFactor])

def learn(x, y, z):
    # get tiles associated with the position -> Features 
    tiles = mytiles(x, y)
    estimate = 0
    #for each feature, add up all the weights 
    for tile in tiles:
        estimate += weights[tile]                  #form estimate estimate is based on weights 
    error = z - estimate                           # this is the error that this example 
    #subtract the estimate from the target
    #updatae the weights for this 
    for tile in tiles:
        weights[tile] += stepSize * error          #learn weights



def test(x, y):
    tiles = mytiles(x, y)
    estimate = 0
    for tile in tiles:
        estimate += weights[tile]
    return estimate 

print(mytiles(0,0))
print(mytiles(0,0.01)) 