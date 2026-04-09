#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11279                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11279                          #+#        #+#      #+#     #
#    Solved: 2026/04/06 13:12:20 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq

# heapq.heappop()은 가장 작은 원소를 반환하기 때문에
# heappush()할 때, -부호를 붙여 저장
heap = []

for _ in range(int(sys.stdin.readline())):
    cmd = int(sys.stdin.readline())
    if cmd == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -cmd)