#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1238                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1238                           #+#        #+#      #+#     #
#    Solved: 2026/04/22 03:43:14 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from heapq import heappop, heappush

def dijkstra(length, start, graph):
    dist = [float('INF')] * (length+1)
    # 시작 정점
    dist[start] = 0

    queue = []
    heappush(queue, (0, start))
    while queue:
        d, now = heappop(queue)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heappush(queue, (cost, i[0]))

    return dist

vortex, edge, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(vortex + 1)]
reverse_graph = [[] for _ in range(vortex + 1)]

for _ in range(edge):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))
    reverse_graph[e].append((s, w))

dist_to_party = dijkstra(vortex, x, graph)
dist_from_party = dijkstra(vortex, x, reverse_graph)

max_time = 0
for i in range(1, vortex + 1):
    total = dist_to_party[i] + dist_from_party[i]
    if total != float('INF'):
        max_time = max(max_time, total)

print(max_time)