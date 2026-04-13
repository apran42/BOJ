#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7662                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7662                           #+#        #+#      #+#     #
#    Solved: 2026/04/13 11:46:58 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq as hq

input = sys.stdin.readline

for _ in range(int(input())):
    max_heap = []
    min_heap = []
    cmd_count = int(input())
    
    visited = [False] * cmd_count 
    
    for i in range(cmd_count):
        line = input().split()
        if not line: continue
        command, num = line[0], int(line[1])
        
        if command == 'I':
            hq.heappush(min_heap, (num, i))
            hq.heappush(max_heap, (-num, i))
            visited[i] = True
            
        elif command == 'D':
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    hq.heappop(max_heap)
                if max_heap:
                    _, idx = hq.heappop(max_heap)
                    visited[idx] = False
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    hq.heappop(min_heap)
                if min_heap:
                    _, idx = hq.heappop(min_heap)
                    visited[idx] = False

    
    while max_heap and not visited[max_heap[0][1]]:
        hq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        hq.heappop(min_heap)
        
    if not max_heap or not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])