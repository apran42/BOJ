#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25595                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25595                          #+#        #+#      #+#     #
#    Solved: 2026/03/26 11:33:47 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
num = int(input())
sinei = -1
region = []

for i in range(num):
    line = list(map(int, input().split()))
    for l_index, l in enumerate(line):
        if l == 1:
            region.append((i+l_index)%2)
        if l == 2:
            sinei = (i+l_index)%2

if sinei in region:
    print('Kiriya')
else:
    print('Lena')