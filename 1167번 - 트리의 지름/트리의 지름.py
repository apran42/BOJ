#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1167                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1167                           #+#        #+#      #+#     #
#    Solved: 2026/04/22 03:42:35 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)

    distance = [-1]*(nodes+1)
    distance[start] = 0

    while queue:
        cur = queue.popleft()

        for child, weight in graph[cur]:
            if distance[child] == -1:
                distance[child] = distance[cur] + weight
                queue.append(child)

    max_dist = 0
    farthest_node = start
    for i in range(1, nodes + 1):
        if distance[i] > max_dist:
            max_dist = distance[i]
            farthest_node = i
            
    return farthest_node, max_dist

nodes = int(sys.stdin.readline())

graph = [[] for _ in range(nodes+1)]

for _ in range(nodes):
    line = list(map(int, sys.stdin.readline().split()))
    vortex = line[0]
    for i in range(1, len(line)-1, 2):
        c, w = line[i], line[i+1]
        graph[vortex].append((c, w))

node_a, _ = bfs(1)
_, diameter = bfs(node_a)

print(diameter)