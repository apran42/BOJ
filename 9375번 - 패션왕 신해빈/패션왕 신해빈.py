#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9375                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9375                           #+#        #+#      #+#     #
#    Solved: 2026/03/30 11:53:01 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

test_case = int(sys.stdin.readline()) 

for _ in range(test_case):
    clothes = int(sys.stdin.readline())
    closet = dict()
    answer = 1
    for _ in range(clothes):
        _, category = sys.stdin.readline().split()
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1
    for c in closet.values():
        answer *= (c+1)
    print(answer-1)