import numpy as np

arr = np.arange(1, 13).reshape(3, 4)
# print(arr)
# # sum 
# out = np.sum(arr, axis=0)
# # max
# out1  = np.max(arr, axis=0)
# print(out, out1)

# # round
# a = 3.5 # 3>odd
# b = 4.5 # 4>even
# print(round(a, 0))
# print(round(b, 0))
print(np.round(arr, 2))