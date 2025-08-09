import sys
import numpy as np

np.random.seed(42)
np.abs(np.random.randn(1000))
if __name__ == "__main__":
    print("Random numbers generated and absolute values taken.")
    print("First 10 values:", np.abs(np.random.randn(10)))
    sys.exit(0) 

