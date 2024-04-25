
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    lists=numpy.array(arr,dtype=float)
    return lists[::-1]
arr = input().strip().split(' ')
result = arrays(arr)
print(result)