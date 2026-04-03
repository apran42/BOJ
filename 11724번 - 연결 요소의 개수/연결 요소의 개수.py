#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11724                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11724                          #+#        #+#      #+#     #
#    Solved: 2026/04/02 15:11:24 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

vortex, line = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(vortex+1)]
connection = 0

for _ in range(line):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (vortex + 1)
for i in range(1, vortex+1):
    if not visited[i]:
        connection += 1

        queue = [i]
        visited[i] = True
        head = 0

        while head < len(queue):    
            current = queue[head]
            head += 1
            
            for n in graph[current]: 
                if not visited[n]:
                    visited[n] = True
                    queue.append(n)

print(connection)