#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9663                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9663                           #+#        #+#      #+#     #
#    Solved: 2026/04/22 03:44:01 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def n_queen(x):
    global answer

    if x == n:
        answer += 1
        return

    for i in range(n):
        row[x] = i
        if is_promising(x):
            n_queen(x+1)
n = int(sys.stdin.readline())

row = [0] * n
answer = 0
n_queen(0)
print(answer)