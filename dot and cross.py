# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n=int(input())
a=numpy.array([input().split()for _ in range(n)],int)
b=numpy.array([input().split()for _ in range(n)],int)
m=numpy.dot(a,b)
print(m)
import numpy
print(str(numpy.eye(*map(int(input().split()))).replace('1','1').replace('0','0')))