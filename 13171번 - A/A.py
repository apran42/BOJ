#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13171                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13171                          #+#        #+#      #+#     #
#    Solved: 2026/04/09 13:08:11 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
DIVISION = 1_000_000_007

a = int(input())
x = int(input())

templet = [[1,a%DIVISION]]

i = 2
while i <= x:
    templet.append([i, templet[-1][1]**2%DIVISION])
    i *= 2

answer = 1

for exp, num in templet[::-1]:
    if x >= exp:
        x -= exp
        answer = (answer*num)%DIVISION

print(answer%DIVISION)