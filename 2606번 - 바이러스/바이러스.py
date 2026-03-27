#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2606                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2606                           #+#        #+#      #+#     #
#    Solved: 2026/03/27 11:43:36 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
computer = int(input())
link = int(input())

graph = [[] for _ in range(computer+1)]

# 인접 리스트
for _ in range(link):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)

# 방문했는가    
visited = [False] * (computer + 1)

# 1번 컴퓨터
queue = [1]
visited[1] = True

# 방문할 컴퓨터를 나타내는 큐의 포인터
head = 0

# 방문할 큐보다 포인터가 커질 때까지(더 이상 방문할 컴퓨터가 없을 때까지)
while head < len(queue):    
    current = queue[head]   # 현재 컴퓨터의 번호
    head += 1 # 포인터 증가
    
    for n in graph[current]:    # 현재 컴퓨터와 연결된 모든 컴퓨터
        if not visited[n]:
            visited[n] = True
            queue.append(n) # 방문하지 않았으면 새롭게 큐에 추가
# 1번을 제외한 큐(1번과 연결된 컴퓨터의 수)
print(len(queue) - 1)