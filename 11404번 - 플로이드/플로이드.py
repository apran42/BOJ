#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11404                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11404                          #+#        #+#      #+#     #
#    Solved: 2026/04/22 03:44:21 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

city = int(input())
bus = int(input())
INF = float('INF')
graph = [[INF] * (city + 1) for _ in range(city + 1)]

for a in range(1, city + 1):
    graph[a][a] = 0

for _ in range(bus):
    start, end, cost = map(int, input().split())
    if cost < graph[start][end]:
        graph[start][end] = cost

for k in range(1, city + 1):
    for i in range(1, city + 1):
        for j in range(1, city + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, city + 1):
    for j in range(1, city + 1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()