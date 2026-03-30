#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9095                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9095                           #+#        #+#      #+#     #
#    Solved: 2026/03/30 11:13:16 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# n=1 일 때 경우(1): 1가지
# n=2 일 때 경우(1+1, 2): 2가지
# n=3 일 때 경우(1+1+1, 1+2, 2+1, 2+2): 4가지

dp = [0, 1, 2, 4]

test_case = int(input())
for _ in range(test_case):
    num = int(input())
    if len(dp)-1 < num:
        for _ in range(len(dp), num+1):
            dp.append(dp[-1]+dp[-2]+dp[-3])
    print(dp[num])
