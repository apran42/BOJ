#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30007                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30007                          #+#        #+#      #+#     #
#    Solved: 2025/09/26 00:55:30 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a,b,x = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(a*(x-1)+b)+'\n')