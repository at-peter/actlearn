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

    max_iteration = 100
    num_steps = 1000
    environment = initialize()
    
    agent = agent()
    # for n in range(max_iteration):
    #     total_reward = 0 
    #     print(n)
    #     for i in range(num_steps):
    #         observation = environment.reset()
    #         environment.render()
    #         action = agent.act(observation)
    #         print('Action:', action, i)
    #         observation, reward, done, info = environment.step([action])
    #         # TODO: should have a check if the episode is done. 
    #         total_reward += reward
    #         works = agent.learn(observation, reward)
    #         # print(done)

    #         if done:
    #             print('Agent actually got to the end')
    #             print(total_reward, 'For trial:', n)
    #             break
    #         if i == num_steps - 1:
    #             print('agent timed out')
    #             print(total_reward, 'for trial', n)
    #             break
    # environment.close()
    total_reward = 0 
    observation = environment.reset()

    # for i in range(100):
    action = 1
    observation, reward, done, info = environment.step([action])
    agent.learn(observation,reward)
    observation , reward, done, info = environment.step([action])
    agent.learn(observation, reward)
    print(agent.weights[0:20])
    



