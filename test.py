import sys
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
np.abs(np.random.randn(1000))
plt.hist(np.abs(np.random.randn(1000)), bins=30, density=True, alpha=0.6, color='g')
plt.title('Histogram of Absolute Values of Random Numbers')
plt.xlabel('Value')

