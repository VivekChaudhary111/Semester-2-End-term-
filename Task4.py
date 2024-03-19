import numpy as np
n, m = map(int, input().split())
ls1 = []
ls2 = []
for i in range(n):
    ls = list(map(int, input().split()))
    ls1.append(ls)
for i in range(n):
    ls = list(map(int, input().split()))
    ls2.append(ls)

print( 'Add the two arrays:' )
print (np.add(ls1,ls2) )
print ('Subtract the two arrays:' )
print (np.subtract(ls1,ls2))
print ('Multiply the two arrays:' )
print (np.multiply(ls1,ls2) )
print ('Floor divide of the two arrays:')
print (np.floor_divide(ls1,ls2))
print('Mod of two arrays:')
print(np.mod(ls1,ls2))
print('Power of two arrays:')
print(np.power(ls1,ls2))