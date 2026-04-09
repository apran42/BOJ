#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3097                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3097                           #+#        #+#      #+#     #
#    Solved: 2026/04/09 11:51:40 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
pos = []
last_x_pos, last_y_pos = 0, 0
for _ in range(n):
    dot_x, dot_y = map(int, input().split())
    last_x_pos += dot_x
    last_y_pos += dot_y
    pos.append([dot_x, dot_y])

print(last_x_pos, last_y_pos)
deleted = []

for x, y in pos:
    after_x_pos, after_y_pos = last_x_pos-x, last_y_pos-y
    deleted.append((after_x_pos**2+after_y_pos**2)**(0.5))
answer = min(deleted)
print(f"{answer:.2f}")