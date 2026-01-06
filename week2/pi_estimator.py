import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(N: int) -> float:
    x_coords = np.random.uniform(-1,1, size = N)
    y_coords = np.random.uniform(-1,1, size = N)
    dist = x_coords ** 2 + y_coords ** 2
    outside = dist > 1
    count = np.sum(outside)
    return 4*(N-count)/N

N_values = np.logspace(1, 7, num=7)
N_values = N_values.astype(int)
estimates = []
for value in N_values:
    est = estimate_pi(value)
    estimates.append(est)

estimates = np.array(estimates)
act = np.pi
percent_error = np.abs(estimates - act) / act * 100

plt.figure()
plt.plot(N_values, estimates, marker='o', label='Estimated π')
plt.axhline(y=np.pi, linestyle='--', label='True π')

plt.xscale('log')
plt.xlabel('Number of points (N)')
plt.ylabel('Estimated π')
plt.title('Monte Carlo Estimation of π')
plt.legend()
plt.grid(True)

plt.show()

plt.figure()
plt.plot(N_values, percent_error, marker='o')

plt.xscale('log')
plt.xlabel('Number of points (N)')
plt.ylabel('Percent Error (%)')
plt.title('Percent Error of Monte Carlo π Estimation')
plt.grid(True)

plt.show()
