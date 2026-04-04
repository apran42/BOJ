#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1931                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1931                           #+#        #+#      #+#     #
#    Solved: 2026/04/03 16:56:56 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
reservations = []
count = 0

for _ in range(n):
    reservations.append(list(map(int, input().split())))

reservations.sort(key=lambda x:(x[1], x[0]))
last_end_time = 0

for start, end in reservations:
    if last_end_time <= start:
        count += 1
        last_end_time = end

print(count)