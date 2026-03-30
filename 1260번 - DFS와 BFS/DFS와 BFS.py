#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1260                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1260                           #+#        #+#      #+#     #
#    Solved: 2026/03/30 12:07:29 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(2000)

def dfs(vortex, graph, visited):
    visited[vortex] = True
    print(vortex, end= ' ')

    for neighbor in graph[vortex]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)
    
    
def bfs(vortex, graph, visited):
    visited_vortexs = [vortex]
    queue = [vortex]
    visited[vortex] = True
    pointer = 0
    
    while pointer < len(queue):
        current = queue[pointer]
        pointer += 1

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                visited_vortexs.append(neighbor)
                queue.append(neighbor)
    print(*visited_vortexs)


n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

# 인접 정점을 오름차순으로
for g in graph:
    g.sort()

visited = [False] * (n + 1)

dfs(vortex=v, graph=graph, visited=visited)
print()
# 정점 방문 리스트 초기화
visited = [False] * (n + 1)
bfs(vortex=v, graph=graph, visited=visited)