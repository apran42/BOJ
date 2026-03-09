#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11399                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11399                          #+#        #+#      #+#     #
#    Solved: 2026/02/21 17:50:12 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
people = int(input())
times = list(map(int, input().split()))

times.sort()
answer = 0
temp = 0
for t in times:
    temp += t
    answer += temp

print(answer)