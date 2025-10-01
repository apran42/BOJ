#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 29332                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/29332                          #+#        #+#      #+#     #
#    Solved: 2025/10/01 13:37:57 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n = int(sys.stdin.readline())
max_x, min_x, max_y, min_y = 10**10, -10**10, 10**10, -10**10
count = [False]*4  # 각 방향(L, R, D, U)이 주어졌는지 체크하기 위한 리스트

for _ in range(n):
    x, y, d = sys.stdin.readline().rstrip().split()
    x, y = int(x), int(y)
    
    if d == 'L':
        max_x = min(max_x, x-1)  # L은 x를 1 감소시키므로 max_x 갱신
        count[0] = True
    if d == 'R':
        min_x = max(min_x, x+1)  # R은 x를 1 증가시키므로 min_x 갱신
        count[1] = True
    if d == 'D':
        max_y = min(max_y, y-1)  # D는 y를 1 감소시키므로 max_y 갱신
        count[2] = True
    if d == 'U':
        min_y = max(min_y, y+1)  # U는 y를 1 증가시키므로 min_y 갱신
        count[3] = True

# 모든 방향이 주어졌는지 확인
if min_x > max_x or min_y > max_y:
    sys.stdout.write('0')
elif False in count:
    sys.stdout.write('Infinity')
else:
    result = (max_x - min_x + 1) * (max_y - min_y + 1)
    sys.stdout.write(str(result))