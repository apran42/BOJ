#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2178                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2178                           #+#        #+#      #+#     #
#    Solved: 2026/04/09 13:31:53 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

maze = [list(map(int, list(input()))) for _ in range(n)]

start = maze[0][0]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

queue = [[0,0]]

while queue:
    current_y, current_x = queue.pop(0)

    for i in range(4):
        nx, ny = current_x+dx[i], current_y+dy[i]

        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0 and maze[ny][nx] != 0:
            visited[ny][nx] = visited[current_y][current_x] + 1
            queue.append([ny, nx])

print(visited[-1][-1])