#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2579                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2579                           #+#        #+#      #+#     #
#    Solved: 2025/11/10 15:07:08 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))
if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0]+stairs[1])
else:
    dp = [[stairs[0],stairs[0]],[stairs[0]+stairs[1],stairs[1]]]
    for i in range(2, n):
        dp.append([dp[i-1][1]+stairs[i],max(dp[i-2][0],dp[i-2][1])+stairs[i]])
    print(max(dp[-1][0],dp[-1][1]))