import numpy

n,m,b=list(map(int,input().split()))
arr=numpy.array([input().split() for _ in range(n+m)],int)
print(arr)
#print(numpy.concatenate(arr,axis=0))

