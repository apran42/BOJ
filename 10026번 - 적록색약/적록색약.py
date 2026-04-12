#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10026                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10026                          #+#        #+#      #+#     #
#    Solved: 2026/04/12 10:24:21 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(color, r, c):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = True

    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(4):
            nr, nc = cur_r + dy[i], cur_c+dx[i]

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == color:
                queue.append([nr, nc])
                visited[nr][nc] = True

n = int(input())

# 일반인
grid = [[char for char in input().rstrip()] for _ in range(n)]
visited = [[False] * n for _ in range(n)]
noraml = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(grid[i][j], i, j)
            noraml += 1

# 적록색약
visited = [[False] * n for _ in range(n)]
blind = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(grid[i][j], i, j)
            blind += 1
print(noraml, blind)