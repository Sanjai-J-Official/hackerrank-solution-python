#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter


if __name__ == '__main__':
    nm = list(map(int,input().split()))
    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for i in range(n):
        arr += [list(map(int,input().split()))]
    

    k = int(input())
    sorter_list=sorted(arr,key=itemgetter(k))
    for i in sorter_list:
        print(*i)
