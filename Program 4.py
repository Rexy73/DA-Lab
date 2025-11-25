import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean = 50
std_dev = 10

# Generate samples
samples = np.random.normal(mean, std_dev, 1000)

# Plot histogram
plt.figure(figsize=(8, 6))
plt.hist(samples, bins=30, density=True, alpha=0.6, color="blue")

# Create x range for the normal curve
x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 100)

# Plot normal PDF
plt.plot(x, norm.pdf(x, mean, std_dev), 'r', lw=2, label='Normal Distribution')

# Labels and formatting
plt.title('Normal Distribution Example (Quality Control)')
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

plt.show()
