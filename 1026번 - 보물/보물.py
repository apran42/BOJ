#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1026                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1026                           #+#        #+#      #+#     #
#    Solved: 2026/02/21 17:34:53 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)

answer = 0
for i in range(n):
    answer += a_list[i]*b_list[i]
print(answer)