import numpy as np
ls = list(map(int, input().split()))
ls2 = ls[::-1]
arr = np.array(ls2, dtype="float")
print(arr)
