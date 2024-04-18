

import math
import os
import random
import re
import sys
from collections import Counter

'''

sorted fuction used for sorting the string

for example:

input>>>

bcaefgdh

output>>>>

abcdefgh

//////////////////

collection package can import to Counter lib,counter using for
count to allocated the values

for example :
input>>>>>

aabbbccde

Output>>>>>

 
Counter({'b': 3, 'a': 2, 'c': 2, 'd': 1, 'e': 1})

////////////////////

most_common function using for common letter to orderwise

we can one arggument pass most_common(n)

 
'''


if __name__ == '__main__':
    s = sorted(input())
    #print(s)
    z=Counter(s)
    #print(z)
    z=Counter(s).most_common(3)
    print(z)
    for i in z:
        print(*i)
