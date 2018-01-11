from time import time
import numpy as np

a = np.arange(100000000, dtype=np.uint64)

start = time()
print(sum(a))
print(time()-start)

start = time()
print(a.sum())
print(time()-start)
