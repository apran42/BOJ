#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1012                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1012                           #+#        #+#      #+#     #
#    Solved: 2026/04/02 13:34:05 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
t = int(input())

# 상하좌우 벡터
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0 for _ in range(m)] for _ in range(n)]
    # 방문했는지
    visited = [[False] * m for _ in range(n)] 
    # 지렁이
    worm = 0
    # 큐
    queue = []

    for _ in range(k):
        j, i = map(int, input().split())
        farm[i][j] = 1

    for r in range(n):
        for c in range(m):
            if farm[r][c] == 1 and not visited[r][c]:
                worm += 1
                queue.append([r,c])
                visited[r][c] = True
                # bfs 로직
                while queue:
                    current_r, current_c = queue.pop(0)

                    for i in range(4):
                        nr = current_r + dy[i]
                        nc = current_c + dx[i]

                        if 0 <= nr < n and 0 <= nc < m:
                            if farm[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append([nr,nc])
    print(worm)