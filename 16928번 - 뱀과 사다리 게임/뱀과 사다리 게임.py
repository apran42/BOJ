#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16928                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16928                          #+#        #+#      #+#     #
#    Solved: 2026/04/13 10:24:05 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

ladder, snake = map(int, sys.stdin.readline().rsplit())
distance = [-1] * 101
board = [i for i in range(101)]

for _ in range(ladder+snake):
    start, end = map(int, sys.stdin.readline().rsplit())
    board[start] = end

queue = deque()
queue.append(1)
distance[1] = 0

while queue:
    current = queue.popleft()

    for dice in range(1, 7):
        temp = current + dice
        # 아직 게임 진행 중
        if temp <= 100:
            real_next = board[temp]
            if distance[real_next] == -1:
                distance[real_next] = distance[current] + 1
                queue.append(real_next)

sys.stdout.write(str(distance[-1]))