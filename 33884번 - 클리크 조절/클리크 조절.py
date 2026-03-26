#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 33884                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/33884                          #+#        #+#      #+#     #
#    Solved: 2026/03/20 16:01:20 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

ammo = int(sys.stdin.readline())

first, second = [], []

# input 대신 sys.stdin.readline()을 사용하여 입력 시간을 줄임
for _ in range(ammo):
    first.append(list(map(int, sys.stdin.readline().rstrip().split())))

for _ in range(ammo):
    second.append(list(map(int, sys.stdin.readline().rstrip().split())))

first_x, first_y = max(first)
second_x, second_y = max(second)

print(second_x-first_x, second_y-first_y)