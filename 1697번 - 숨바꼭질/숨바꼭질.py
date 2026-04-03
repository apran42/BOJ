#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1697                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1697                           #+#        #+#      #+#     #
#    Solved: 2026/04/03 16:04:34 by flyingdisc1   ###          ###   ##.kr     #
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
    for next_step in (current - 1, current + 1, 2*current):
        if 0 <= next_step <= 100000 and visited[next_step] == -1:
            visited[next_step] = visited[current] + 1
            queue.append(next_step)