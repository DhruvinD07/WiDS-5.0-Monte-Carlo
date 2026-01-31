from blackjack_env import BlackJackEnv
from collections import defaultdict
import random
import matplotlib.pyplot as plt
import numpy as np

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

window = 5000
rolling_avg = np.convolve(
    rewards,
    np.ones(window) / window,
    mode="valid"
)

plt.figure()
plt.plot(rolling_avg)
plt.xlabel("Episode")
plt.ylabel("Rolling Average Reward")
plt.title("Learning Curve (Monte Carlo Control)")
plt.savefig("learning_curve_mc_control.png", dpi=300, bbox_inches="tight")
plt.close()

def get_policy(player_sum, dealer_card, usable_ace):
    state = (player_sum, dealer_card, usable_ace)
    return max([0, 1], key=lambda a: Q[(state, a)])

def plot_strategy(usable_ace, filename):
    policy = np.zeros((10, 10))

    for ps in range(12, 22):
        for dc in range(1, 11):
            policy[ps - 12, dc - 1] = get_policy(ps, dc, usable_ace)

    plt.figure()
    plt.imshow(policy, origin="lower")
    plt.colorbar(ticks=[0, 1])
    plt.clim(-0.5, 1.5)
    plt.xlabel("Dealer Showing")
    plt.ylabel("Player Sum")
    plt.xticks(range(10), range(1, 11))
    plt.yticks(range(10), range(12, 22))
    plt.title("Usable Ace" if usable_ace else "No Usable Ace")
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()

plot_strategy(True, "policy_usable_ace.png")
plot_strategy(False, "policy_no_usable_ace.png")
