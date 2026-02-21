#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2156                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2156                           #+#        #+#      #+#     #
#    Solved: 2025/11/11 14:01:46 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0]+wine[1])
else:
    