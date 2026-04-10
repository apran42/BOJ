#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1389                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1389                           #+#        #+#      #+#     #
#    Solved: 2026/04/10 11:09:16 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())
inf = float('INF')
graph = [[inf] * (n+1) for _ in range(n+1)]

# 자기 자신
for i in range(1, n+1):
    graph[i][i] = 0
# 인접 노드
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드-워셜 알고리즘
for i in range(1, n+1): # 거쳐가는 노드
    for j in range(1, n+1): # 출발 노드
        for k in range(1, n+1): # 도착 노드
            # 출발->도착과 출발->중간->도착 중 최솟값
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]

result = []

for i in range(1, n+1):
    total = sum(graph[i][1:]) # 무한대값 패스
    result.append(total)
# 값이 가장 작은 사람 중복의 경우 인덱스가 작은 사람
print(result.index(min(result))+1)