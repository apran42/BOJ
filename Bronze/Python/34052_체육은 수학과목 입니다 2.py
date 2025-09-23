from sys import stdin

time = 0
for _ in range(4):
    time += int(stdin.readline())
if 1800 - time >= 300:
    print('Yes')
else:
    print('No')