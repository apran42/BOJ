#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 33990                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/33990                          #+#        #+#      #+#     #
#    Solved: 2025/10/01 12:01:49 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n = int(sys.stdin.readline())
students = []
for _ in range(n):
    one_rm = list(map(int, sys.stdin.readline().split()))
    if sum(one_rm) >= 512:
        students.append(sum(one_rm))
sys.stdout.write('-1' if len(students) == 0 else str(min(students)))