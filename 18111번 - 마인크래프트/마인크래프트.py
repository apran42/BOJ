#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18111                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18111                          #+#        #+#      #+#     #
#    Solved: 2026/04/09 15:03:39 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import Counter

row, col, block = map(int, input().split())

ground = []
max_height, min_height = float('-INF'), float('INF')

for _ in range(row):
    ground += list(map(int, input().split()))

height_counts = Counter(ground)
minimum_time = float('INF')
highest = 0

for height in range(0, 257):
    need_to_add, need_to_dig = 0, 0

    for h, count in height_counts.items():
        if h > height:
            need_to_dig += (h-height)*count
        else:
            need_to_add += (height - h)*count

    if block + need_to_dig >= need_to_add:
        current_time = need_to_dig*2 + need_to_add

        if current_time <= minimum_time:
            minimum_time = current_time
            highest = height

print(minimum_time, highest)
