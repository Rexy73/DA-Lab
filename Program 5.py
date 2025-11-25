# Exponential Distribution - Reliability Analysis example
# Simulating and plotting an exponential distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Correct scale parameter
exp_samples = np.random.exponential(scale=2, size=1000)

plt.figure(figsize=(8, 6))
plt.hist(exp_samples, bins=30, density=True, alpha=0.6, color='green')

x_exp = np.linspace(0, 10, 100)
plt.plot(x_exp, expon.pdf(x_exp, scale=2), 'r-', lw=2, label='Exponential Distribution')

plt.title('Exponential Distribution Example (Reliability Analysis)')
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
