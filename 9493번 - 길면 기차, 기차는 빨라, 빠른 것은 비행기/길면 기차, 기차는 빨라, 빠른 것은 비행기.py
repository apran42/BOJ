#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9493                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9493                           #+#        #+#      #+#     #
#    Solved: 2026/04/16 09:37:16 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

while True:
    dis, train, airplane = map(int, sys.stdin.readline().split())
    if dis == 0 and train == 0 and airplane == 0:
        break
    train_time, airplane_time = dis/train, dis/airplane
    diff = int(round((train_time - airplane_time)*3600))
    hour = diff // 3600
    minute = (diff % 3600) // 60
    second = diff % 60
    print(f'{hour}:{minute:02d}:{second:02d}')