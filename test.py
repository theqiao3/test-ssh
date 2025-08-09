import sys
import numpy as np
import matplotlib.pyplot as plt

data = np.array([2023, 10, 1])
plt.figure(figsize=(10, 5))
plt.plot(data, marker='o', linestyle='-', color='b')
plt.title('Data Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()

