import sys


N = int(input())
win = -1
for i in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    tmp_li = sorted(li[2:], reverse=True)
    tmp_scr = max(li[:2]) + sum(tmp_li[:2])
    if tmp_scr >= win:
        win = tmp_scr
print(win)