#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11726                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11726                          #+#        #+#      #+#     #
#    Solved: 2026/03/30 11:44:07 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

input = sys.stdin.readline

n = int(input())
dp = [0, 1, 2]
for _ in range(2, n):
    dp.append((dp[-1]+dp[-2])%10007)
print(dp[n])