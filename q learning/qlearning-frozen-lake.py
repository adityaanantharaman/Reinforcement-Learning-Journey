# -*- coding: utf-8 -*-
"""qlearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o6t7A2ggtjQSW1CWNcBEuPRBnRTeitie
"""

!pip install gym

import numpy as np
import gym
import random

env = gym.make("FrozenLake-v0")

action_size=env.action_space.n
state_size=env.observation_space.n

print(state_size,action_size)

qtable=np.zeros((state_size,action_size))
qtable

"""# Initialize the parameters:"""

total_episodes=25000
learning_rate=0.8
max_steps=99
gamma=0.90 # Discounting rate

epsilon=1 # Exploraton rate
max_epsilon=1
min_epsilon=0.01
decay_rate=0.01 # Exponential decay rate for exploration prob

"""# The Q learning algirithm:"""

rewards=[]
for episode in range(total_episodes):
  state=env.reset()
  step=0
  done=False
  total_rewards=0
  
  for step in range(max_steps):
    exp_exp_tradeoff=random.uniform(0,1)
    if exp_exp_tradeoff>epsilon:
      action=np.argmax(qtable[state,:])
    else:
      action=env.action_space.sample()
    
    new_state,reward,done,info=env.step(action)
    
    qtable[state,action]+=learning_rate*(reward+gamma*(np.max(qtable[new_state,:]))-qtable[state,action]) # Updating Q table values 
    
    total_rewards+=reward
    state=new_state
    
    if done==True:
      break
      
  epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode) 
  rewards.append(total_rewards)
  
print("score over time : "+str(sum(rewards)/total_episodes))
print(qtable)

for episode in range(10):
  state=env.reset()
  step=0
  done=False
  print("****************************************************")
  print("EPISODE ", episode)
  for step in range(max_steps):
    action=np.argmax(qtable[state,:])
    new_state,reward,done,info=env.step(action)
    if done:
      env.render()
      print("number of steps : "+str(step))
      break
    state=new_state
env.close()

