#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14940                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14940                          #+#        #+#      #+#     #
#    Solved: 2026/04/03 16:20:24 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

queue = deque()
# 상하좌우 벡터
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        # 시작 지점
        if graph[i][j] == 2:
            queue.append((i,j))
            distance[i][j] = 0
        # 애초에 갈 수 없는 곳
        elif graph[i][j] == 0:
            distance[i][j] = 0

while queue:
    x, y = queue.popleft()

    # 상하좌우 확인
    for i in range(4):
        near_x, near_y = x+dx[i], y+dy[i]

        # 알맞은 범위 안의 상하좌우이면서 계산하지 않은(방문하지 않은 경우)
        if 0 <= near_x < n and 0 <= near_y < m and distance[near_x][near_y] == -1:
            distance[near_x][near_y] = distance[x][y] + 1
            queue.append((near_x, near_y))

for row in distance:
    print(*row)