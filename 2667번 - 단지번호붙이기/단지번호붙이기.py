#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2667                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2667                           #+#        #+#      #+#     #
#    Solved: 2026/04/10 16:04:29 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(r, c):
    global grid, visited, dx, dy

    queue = deque()
    queue.append([r, c])
    visited[r][c] = True
    houses = 1

    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(4):
            nr, nc = cur_r+dy[i], cur_c+dx[i]

            if (0 <= nr < n and 0 <= nc < n and
                grid[nr][nc] == 1 and not visited[nr][nc]):
                queue.append([nr, nc])
                visited[nr][nc] = True
                houses += 1
    return houses

n = int(input())

grid = [[int(char) for char in input().rstrip()] for _ in range(n)]
visited = [[False] * n for _ in range(n)]
group = 0
houses = []
# 집일 경우에만 bfs
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            group += 1
            houses.append(bfs(i, j))
print(group)
for ans in sorted(houses):
    print(ans)