import sys

n = sys.stdin.readline().rstrip()
digits = len(n)
count = 0

while len(str(int(n)*2)) == digits:
    n = str((int(n)*2))
    count += 1

print(count)