#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16488                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16488                          #+#        #+#      #+#     #
#    Solved: 2025/10/02 00:40:30 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline
output = sys.stdout.write
n, m = map(int,input().split())
# A(0,h), B(-a,0), C(a,0), Pi(p,0)이라 하자.
# 임의의 점 Pi에 대해
# APi^2 = p^2 + h^2
# BPi = |p-(-a)|, CPi = |a-p|
# APi^2 + (BPi * CPi)
# = p^2 + h^2 + (a+p)*(a-p) = p^2 + h^2 + a^2 - p^2
# = h^2 + a^2 = AB^2(n) = AC^2 (이등변 삼각형이므로)
answer = n**2*m
output(str(answer))