from blackjack_env import BlackJackEnv
from collections import defaultdict
import random

env = BlackJackEnv()

Q = defaultdict(float)

epsilon = 0.1
alpha = 0.01
NUM_EPISODES = 500_000

def epsilon_greedy(state):
    if random.random() < epsilon:
        return random.choice([0, 1])
    return max([0, 1], key=lambda a: Q[(state, a)])

rewards = []

for _ in range(NUM_EPISODES):
    state = env.reset()
    episode = []
    done = False

    while not done:
        action = epsilon_greedy(state)
        episode.append((state, action))
        state, reward, done = env.step(action)

    G = reward
    rewards.append(G)

    for (s, a) in episode:
        Q[(s, a)] += alpha * (G - Q[(s, a)])
