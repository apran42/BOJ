#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11053                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11053                          #+#        #+#      #+#     #
#    Solved: 2026/04/15 01:24:56 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
num = int(input())
nums = list(map(int, input().split()))
dp = [1] * num
for i in range(num):
    for j in range(i):
        if nums[i] >  nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))