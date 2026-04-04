#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7576                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7576                           #+#        #+#      #+#     #
#    Solved: 2026/04/05 00:33:14 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

m, n = map(int, input().split())
box = []

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

for _ in range(n):
    box.append(list(map(int, input().split())))

queue = deque()

for r in range(n):
    for c in range(m):
        if box[r][c] == 1:
            queue.append([r, c])

day = 0

while queue:
    row, col = queue.popleft()
    for i in range(4):
        nr, nc = row + dy[i], col + dx[i]

        if 0 <= nr < n and 0 <= nc < m and  box[nr][nc] == 0:
            box[nr][nc] = box[row][col] + 1
            queue.append([nr, nc])

day = max(max(row) for row in box)

if any(0 in row for row in box):
    print(-1)
else:
    print(day - 1)