#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 19572                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/19572                          #+#        #+#      #+#     #
#    Solved: 2025/09/26 01:05:19 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

d1, d2, d3 = map(int, sys.stdin.readline().split())

a = round((d1+d2-d3)/2, 2)
b = round((d1-d2+d3)/2, 2)
c = round((-d1+d2+d3)/2, 2)
if a<1.0 or b<1.0 or c<1.0:
    sys.stdout.write("-1")
else:
    sys.stdout.write(f'{1}\n{a} {b} {c}')