from math import ceil
from sys import stdin

N = int(stdin.readline())

for k in range(1, 7):
    if k*(k+1) // 2 >= N:
        print(k)
        exit()

k = (N+27) // 7
print(ceil(k))
