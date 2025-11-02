import sys
import numpy as np
import matplotlib.pyplot as plt

b = np.array([1, 2, 3, 4, 5],[6, 7, 8, 9, 10])
p = np.max(b)
print(p)

data = np.array([2023, 10, 1])
plt.figure(figsize=(10, 5))
plt.plot(data, marker='o', linestyle='-', color='b')
plt.title('Data Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()



# 示例测试
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
c = a + b
print("a + b =", c)


