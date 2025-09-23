#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7785                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7785                           #+#        #+#      #+#     #
#    Solved: 2025/09/24 05:15:44 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n = int(sys.stdin.readline())
employee = set()
for _ in range(n):
    name, cond = sys.stdin.readline().rstrip().split()
    if cond == 'enter':
        employee.add(name)
    if cond == 'leave':
        employee.discard(name)
employee = sorted(list(employee), reverse=True)
for name in employee:
    print(name)