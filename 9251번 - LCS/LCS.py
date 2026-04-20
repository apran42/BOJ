#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9251                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9251                           #+#        #+#      #+#     #
#    Solved: 2026/04/20 11:49:45 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

string_a = sys.stdin.readline().rstrip()
string_b = sys.stdin.readline().rstrip()

dp = [[0] * (len(string_b)+1) for _ in range(len(string_a)+1)]

for i in range(1, len(string_a)+1):
    for j in range(1, len(string_b)+1):
        if string_a[i-1] == string_b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])