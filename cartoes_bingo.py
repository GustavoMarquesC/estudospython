import random
import numpy as np

x = np.random.randint(1, 100, (5, 5))

x[2, 2] = -1

print(x)
