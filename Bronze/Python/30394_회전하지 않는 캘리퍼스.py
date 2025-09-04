N = int(input())
li=[[],[]]
for i in range(N):
    x, y = map(int, input().split())
    li[0].append(x)
    li[1].append(y)
print(max(li[1])-min(li[1]))