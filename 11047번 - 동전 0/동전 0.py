#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11047                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11047                          #+#        #+#      #+#     #
#    Solved: 2025/11/13 09:51:20 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
coin, target = map(int, input().split())
coins = []
for _ in range(coin):
    coins.append(int(input()))
coins.sort(reverse=True)
