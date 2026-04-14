#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11725                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11725                          #+#        #+#      #+#     #
#    Solved: 2026/04/15 01:49:41 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

nodes = int(input())
graph = [[] for _ in range(nodes+1)]
parents = [0] * (nodes+1)
for _ in range(nodes-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1]) # 루트 노드
parents[1] = 1

while queue:
    cur = queue.popleft()

    for n in graph[cur]:
        if parents[n] == 0:
            parents[n] = cur
            queue.append(n)

for p in parents[2:]:
    print(p)