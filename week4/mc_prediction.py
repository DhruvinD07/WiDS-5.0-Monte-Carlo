from blackjack_env import BlackJackEnv
from collections import defaultdict

env = BlackJackEnv()

def policy(state):
    player_sum, dealer_card, usable_ace = state
    return 0 if player_sum >= 20 else 1

returns_sum = defaultdict(float)
returns_count = defaultdict(int)
V = defaultdict(float)

NUM_EPISODES = 10_000

for _ in range(NUM_EPISODES):
    state = env.reset()
    episode_states = []
    done = False

    while not done:
        action = policy(state)
        episode_states.append(state)
        state, reward, done = env.step(action)

    G = reward
    visited = set()

    for s in episode_states:
        if s not in visited:
            visited.add(s)
            returns_sum[s] += G
            returns_count[s] += 1
            V[s] = returns_sum[s] / returns_count[s]

def avg_value(player_sum):
    vals = [v for (ps, _, _), v in V.items() if ps == player_sum]
    return sum(vals) / len(vals)

print("V(Player Sum = 21):", avg_value(21))
print("V(Player Sum = 5):", avg_value(5))
