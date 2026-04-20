#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1753                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1753                           #+#        #+#      #+#     #
#    Solved: 2026/04/20 11:07:15 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from heapq import heappop, heappush

def dijkstra(length, start):
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


vortex, edge = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline())

graph = [[] for _ in range(vortex + 1)]

for _ in range(edge):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append([e, w])

info = dijkstra(vortex, start)

for min_cost in info[1:]:
    if min_cost == float('INF'):
        print('INF')
    else:
        print(min_cost)