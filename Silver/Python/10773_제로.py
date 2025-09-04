import sys

N = int(sys.stdin.readline())
result=[]
for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        result.pop()
    else:
        result.append(tmp)
print(sum(result))