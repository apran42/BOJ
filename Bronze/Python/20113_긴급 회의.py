from sys import stdin

# 초기화
N = int(stdin.readline())

votes = list(stdin.readline().rstrip().split(' '))
voted = [0 for _ in range(N)]
#투표
for vote in votes:
    if vote != '0':
        voted[int(vote)-1] += 1
# 가장 많은 득표수
ejected = max(voted)
#유일하면 그 번호를, 아니면 스킵
if voted.count(ejected) == 1:
    print(voted.index(ejected)+1)
else:
    print('skipped')