#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1912                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1912                           #+#        #+#      #+#     #
#    Solved: 2025/11/07 09:41:25 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
nums = list(map(int, input().split()))
dp = [i for i in nums]
max_num = max(nums)
for index in range(1, n):
    # nums[index] 까지의 최댓값을 저장
    dp[index] = max(dp[index-1] + nums[index], nums[index])

    max_num = max(max_num, dp[index])

print(max_num)

