import gymnasium as gym
from time import sleep

env = gym.make("Breakout-v4", render_mode="human")
env.reset()

for i in range(100):
    env.render()
    st = env.step(env.action_space.sample())
    observation, reward, done, info = st[0], st[1], st[3], st[4]

    if reward != 0:
        print("r :", reward)
    # sleep(0.1)
    if done:
        break
