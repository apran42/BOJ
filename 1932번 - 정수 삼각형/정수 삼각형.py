#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1932                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1932                           #+#        #+#      #+#     #
#    Solved: 2025/11/07 12:33:15 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
triangle = []
for _ in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)
dp = [[triangle[0][0]]]
# 입력 형태에서 윗 라인의 같은 자리와 왼쪽 자리의 최댓값
for i in range(1, n):
    temp_row = []
    for j in range(len(triangle[i])):
        if j == 0:
            temp_row.append(triangle[i][j] + dp[i-1][0])
        elif j == len(triangle[i])-1:
            temp_row.append(triangle[i][j] + dp[i-1][-1])
        else:
            temp_row.append(max(triangle[i][j] + dp[i-1][j-1],
                                triangle[i][j] + dp[i-1][j]))
    dp.append(temp_row)

print(max(dp[-1]))