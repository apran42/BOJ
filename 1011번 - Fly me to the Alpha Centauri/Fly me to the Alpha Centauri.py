#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1011                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1011                           #+#        #+#      #+#     #
#    Solved: 2025/10/08 04:44:48 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    answer = 0
    start, end = map(int, input().split())
    length = end-start
    max_jump = int(length**0.5)
    moved_length = 0
    for i in range(1,max_jump):
        moved_length += i*2
        answer += 2
    for j in range(max_jump, 0, -1):
        dis = length-moved_length
        if length > moved_length:
            temp = dis//j
            moved_length += temp*j
            answer += temp
    sys.stdout.write(str(answer)+'\n')