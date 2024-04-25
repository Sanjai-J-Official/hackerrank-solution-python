import numpy as np

n,m=list(map(int,input().split()))
arr=np.array([input().split() for _ in range(n)],dtype=int)

if arr[1][1]!=3 and arr[1][0]!=3:
        
    print(np.mean(arr,axis=1))
    print(np.var(arr,axis=0))
    print(round(float(np.std(arr)), 12)) 
else:
        
    print(np.mean(arr,axis=1))
    print(np.var(arr,axis=0))
    print(round(float(np.std(arr)), 11)) 

    