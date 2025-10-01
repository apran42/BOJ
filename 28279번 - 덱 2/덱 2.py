#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28279                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28279                          #+#        #+#      #+#     #
#    Solved: 2025/09/30 15:41:50 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()

for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == '1':
        d.appendleft(int(order[1]))
    elif order[0] == '2':
        d.append(int(order[1]))
    elif order[0] == '3':
        sys.stdout.write(str(d.popleft())+'\n' if d else '-1\n')
    elif order[0] == '4':
        sys.stdout.write(str(d.pop())+'\n' if d else '-1\n')
    elif order[0] == '5':
        sys.stdout.write(str(len(d))+'\n')
    elif order[0] == '6':
        sys.stdout.write('0\n' if d else '1\n')
    elif order[0] == '7':
        sys.stdout.write(str(d[0])+'\n' if d else '-1\n')
    elif order[0] == '8':
        sys.stdout.write(str(d[-1])+'\n' if d else '-1\n')
