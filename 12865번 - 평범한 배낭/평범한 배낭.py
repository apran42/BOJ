#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12865                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12865                          #+#        #+#      #+#     #
#    Solved: 2026/04/20 10:29:02 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, can_hold = map(int, input().split())

dp = [0] * (can_hold+1)

for _ in range(n):
    w, v = map(int, input().split())
    for j in range(can_hold, w - 1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[can_hold])