#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11659                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11659                          #+#        #+#      #+#     #
#    Solved: 2026/03/30 11:26:56 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

input = sys.stdin.readline

num, test_case = map(int, input().split())

nums = list(map(int, input().split()))

# 누적합
accumulated_sum = [0]
current_total = 0
for i in range(num):
    current_total += nums[i]
    accumulated_sum.append(current_total)

for _ in range(test_case):
    start, end = map(int, input().split())
    print(accumulated_sum[end]-accumulated_sum[start-1])