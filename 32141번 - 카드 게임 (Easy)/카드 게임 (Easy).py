#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 32141                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/32141                          #+#        #+#      #+#     #
#    Solved: 2025/09/26 01:22:51 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n, h = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

attack = 0
if sum(card) < h:
    sys.stdout.write('-1')
else:
    for index, num in enumerate(card):
        attack += num
        if attack >= h:
            sys.stdout.write(str(index+1))
            break