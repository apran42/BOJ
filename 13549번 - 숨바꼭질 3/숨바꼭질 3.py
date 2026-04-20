#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13549                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13549                          #+#        #+#      #+#     #
#    Solved: 2026/04/20 10:36:58 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

subin, sibling = map(int, input().split())

queue = deque()
queue.append(subin)
visited = [-1] * (100001)
visited[subin] = 0

while queue:
    
    current = queue.popleft()
    # 동생을 만난 경우
    if current == sibling:
        print(visited[current])
        break    
    # 한 점에서 이동 가능한 점
    next_step = current * 2
    if 0 <= next_step <= 100000 and visited[next_step] == -1:
        visited[next_step] = visited[current]
        queue.appendleft(next_step)
        
    # 2. 걷기 (-1, +1) (1초 소요) -> 큐의 맨 뒤에 추가
    for next_step in (current - 1, current + 1):
        if 0 <= next_step <= 100000 and visited[next_step] == -1:
            visited[next_step] = visited[current] + 1
            queue.append(next_step)