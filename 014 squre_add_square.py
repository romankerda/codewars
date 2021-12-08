import math
import sys

def solve(n):
    i,j = 1,1

    while (j+1)*(j+1) - j*j <= n:
        if math.sqrt(n + i) % 1 == 0:
            return i
        j += 1
        i = j * j
    return -1


print(solve(9))