#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1003                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1003                           #+#        #+#      #+#     #
#    Solved: 2025/11/05 00:22:45 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())

fibo = [0, 1]
for _ in range(39):
    fibo.append(fibo[-2] + fibo[-1])

for _ in range(n):
    f = int(input())
    if f == 0:
        print('1 0')
    else:
        print(fibo[f-1], fibo[f])