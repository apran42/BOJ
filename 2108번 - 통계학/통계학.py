#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2108                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2108                           #+#        #+#      #+#     #
#    Solved: 2025/10/17 01:15:31 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import Counter
import sys

N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]
li.sort()

# 1번: 산술 평균
def avg(li):
    return round(sum(li) / len(li))

# 2번: 중앙값
def mid(li):
    return li[len(li) // 2]

# 3번: 최빈값
def mode(li):
    cnt = Counter(li)
    tmp = max(cnt.values())
    modes = [c for c, f in cnt.items() if f == tmp]
    return modes[1] if len(modes) > 1 else modes[0]

# 4번: 범위
def ran(li):
    return max(li) - min(li)

print(avg(li))
print(mid(li))
print(mode(li))
print(ran(li))