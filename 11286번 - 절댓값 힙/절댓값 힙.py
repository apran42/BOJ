#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11286                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11286                          #+#        #+#      #+#     #
#    Solved: 2026/04/12 09:44:45 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import heapq
from sys import stdin, stdout

abs_heap = []

for _ in range(int(stdin.readline())):
    command = int(stdin.readline())

    if command == 0 and not abs_heap:
        stdout.write('0\n')
    elif command == 0:
        abs_num, real_num = heapq.heappop(abs_heap)
        stdout.write(str(real_num)+'\n')
    else:
        heapq.heappush(abs_heap, (abs(command), command))
