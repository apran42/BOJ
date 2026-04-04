#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7569                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7569                           #+#        #+#      #+#     #
#    Solved: 2026/04/05 01:45:06 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())

box = []
queue = deque()

for z in range(h):
    layer = []
    for r in range(n):
        row_data = list(map(int, input().split()))
        for c in range(m):
            if row_data[c] == 1:
                queue.append((z, r, c))
        layer.append(row_data)
    box.append(layer)

# 위, 아래, 상, 하, 좌, 우
dz = [1, -1, 0, 0, 0, 0]
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, -1, 1]

while queue:
    z, r, c = queue.popleft()
    
    for i in range(6):
        nz, nr, nc = z + dz[i], r + dr[i], c + dc[i]
        

        if 0 <= nz < h and 0 <= nr < n and 0 <= nc < m:
            if box[nz][nr][nc] == 0:
                box[nz][nr][nc] = box[z][r][c] + 1
                queue.append((nz, nr, nc))

day = 0
for layer in box:
    for row in layer:
        for tomato in row:
            if tomato == 0:
                print(-1)
                exit()
            day = max(day, tomato)

print(day - 1)