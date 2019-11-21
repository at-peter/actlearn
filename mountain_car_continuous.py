import gym 
import numpy as np
from tdlambagent import agent

def initialize():
    environment_name = 'MountainCarContinuous-v0'
    environment = gym.make(environment_name)
    environment.seed(0)
    np.random.seed()
    max_iteration = 1000
    return environment

if __name__ == '__main__':

    max_iteration = 1000
    num_steps = 500
    environment = initialize()
    
    agent = agent()
    for n in range(max_iteration):
        print(n)
        for i in range(10):
            observation = environment.reset()
            # environment.render()
            action = agent.act(observation)
            print('Action:', action, i)
            observation, reward, done, info = environment.step([action])
            # TODO: should have a check if the episode is done. 
            works = agent.learn(environment, observation, reward)
            # print(done)
            if done:
                print('Agent actually got to the end')
                break
            if i == max_iteration:
                print('agent timed out')
                break
    # environment.close()
    
    # ACTION MUST BE AN ARRAY
    # action = [0.02]
    # observation, reward, done, info = environment.step(action)
    
    # total_reward = 0 
    # for n in range(max_iteration):
    #     environment.render()
    #     action = environment.action_space.sample()
    #     observation, reward, done, info = environment.step(action)
    #     total_reward += reward
    #     if done:
    #         print("Done after {} timesteps".format(n+1))
    #         break
    
    # print("Episode timed out")
    # print(total_reward)
    # environment.close()





    '''
    PSEUDOCODE:
    initialize()
    for n in range(max_iteration):
        for t in range(max_steps):
            action = agent.act()
            observation, reward, done, info = environment.step(action)
            agent.learn()


    '''

