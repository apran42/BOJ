#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1149                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1149                           #+#        #+#      #+#     #
#    Solved: 2025/11/07 09:57:40 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
red, green, blue = [], [], []
for _ in range(n):
    r, g, b = map(int, input().split())
    red.append(r)
    green.append(g)
    blue.append(b)
# 입력 끝!
dp = [[red[0],green[0],blue[0]]]
for i in range(1, n):
    # i번 집에 (r/g/b)를 색칠하는 최솟값
    lowest_red = min(dp[i-1][1], dp[i-1][2]) + red[i]
    lowest_green = min(dp[i-1][0], dp[i-1][2]) + green[i]
    lowest_blue = min(dp[i-1][0], dp[i-1][1]) + blue[i]
    # dp에 저장
    dp.append([lowest_red, lowest_green, lowest_blue])
print(min(dp[-1][0], dp[-1][1], dp[-1][2]))