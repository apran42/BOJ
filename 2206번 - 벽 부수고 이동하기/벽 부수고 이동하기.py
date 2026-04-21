#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2206                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2206                           #+#        #+#      #+#     #
#    Solved: 2026/04/22 03:47:28 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def bfs_3d(g:list):
    # 벽을 안 부순 경우 [][][0], 부순 경우 [][][1] 
    dist = [[[0]*2 for _ in range(col)] for _ in range(row)]
    queue = deque()
    queue.append((0,0,0))
    dist[0][0][0] = 1
    while queue:
        r, c, broken = queue.popleft()

        if r == row-1 and c == col-1:
            print(dist[r][c][broken])
            return

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]

            if 0 <= nr < row and 0 <= nc < col:
                # 벽이 아니고, 방문하지 않은 경우
                if graph[nr][nc] == 0 and dist[nr][nc][broken] == 0:
                    dist[nr][nc][broken] = dist[r][c][broken] + 1
                    queue.append((nr, nc, broken))
                # 벽인데, 벽을 부수지 않은 경우
                elif graph[nr][nc] == 1 and broken == 0:
                    # 벽을 부수고 방문한적이 없으면
                    if dist[nr][nc][1] == 0:
                        dist[nr][nc][1] = dist[r][c][0] + 1
                        queue.append((nr, nc, 1))

    print(-1) # (1, 1) -> (N, M)인 경로가 없음

row, col = map(int, sys.stdin.readline().split())

graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(row)]

bfs_3d(graph)