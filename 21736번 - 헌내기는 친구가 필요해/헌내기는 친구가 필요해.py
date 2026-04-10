#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 21736                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/21736                          #+#        #+#      #+#     #
#    Solved: 2026/04/10 11:07:41 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())

campus = [list(input()) for _ in range(n)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

queue = []
visited = [[False] * m for _ in range(n)]
people = 0

for r_idx, row in enumerate(campus):
    for c_idx, col in enumerate(row):
        if col == 'I':
            queue.append([r_idx, c_idx])
            visited[r_idx][c_idx] = True
        if col == 'X':
            visited[r_idx][c_idx] = True
            
while queue:
    cur_r, cur_c = queue.pop(0)
    
    for i in range(4):
        nr, nc = cur_r+dy[i], cur_c+dx[i]
        
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            queue.append([nr, nc])
            visited[nr][nc] = True
            if campus[nr][nc] == 'P':
                people += 1
                
print(people if people != 0 else 'TT')