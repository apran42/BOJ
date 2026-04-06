#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14501                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14501                          #+#        #+#      #+#     #
#    Solved: 2026/04/06 09:53:19 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

day = int(sys.stdin.readline())
counselings = [list(map(int, sys.stdin.readline().split())) for _ in range(day)]
dp = [0] * (day + 1)

for i in range(day-1, -1, -1):
    period = counselings[i][0]
    money = counselings[i][1]
    if i + period > day:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+period]+money)
print(dp[0])