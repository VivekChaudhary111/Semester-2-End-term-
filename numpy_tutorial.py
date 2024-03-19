import numpy as np
# ls1 = [1, 2, 3, 4]
# ls2 = [1, 300, 4, 5]
# arr1 = np.array(ls1)
# arr2 = np.array(ls2)
# print(arr1, arr2)
# print(ls1, ls2)

# import numpy as np
# import time
# ls  = [1, 2, 3, 4]


# start = time.time()
# arr1 = np.array(ls)
# print(arr1)
# end = time.time()
# print("Arrray Time:", end,start)

# Functions in NumPy

# 1. >>np.array(object, dtype = None, ndmin = 0)

# object: Any object exposing the array interface method returns an array, or any (nested) sequence
# dtype: Desired data type of array, optional
# ndmin: Specifies minimum dimensions of resultant array

# Example 1
# import numpy as np
# a = np.array([1,2,3])
# print(a)
# The output is as follows −
# [1, 2, 3]
#uint = unsigned integer
#int = signed integer
# import numpy as np
# ls =[100, 2, 256]
# arr = np.array(ls, dtype="uint8")  # uint8 ->> (0,255)
# print(arr)
# ls2 =[100, 2, -140]
# arr = np.array(ls2, dtype="int8")  # int8 ->> (0,127) and (-1, -128)
# print(arr)

# ls3 = [4, 6, 8000]
# data = np.array(ls3, dtype='int8')
# print(data)

# This array attribute return a tuple consisting of array dimensions.It can also be used to resize the array
# Example1
# import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# print(a.shape)

# import numpy as np
# arr = np.array([3, 5, 6, 7, 5, 7])
# print(arr.shape)
# print(arr.ndim)
# arr.shape = 3, 2
# print(arr)

# out = arr.reshape((2, 3))
# print(out)
# print(arr)

# Numpy Arange function

# arr = np.arange(1, 10, .1)
# print(arr)

# Mathematical functions
import matplotlib.pyplot as plt
import numpy as np
arr = np.arange(0, 30, .1)
data_sin = 1/np.sin(arr)
# data_cos = np.cos(arr)
# plt.plot(arr, data_cos)
plt.plot(arr, data_sin)

# data_tan = np.tan(arr)
# plt.plot(arr,data_tan)
plt.show()
