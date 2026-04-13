#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9019                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9019                           #+#        #+#      #+#     #
#    Solved: 2026/04/13 14:03:21 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

def moveD(num):
    return (num*2) % 10000
def moveS(num):
    return 9999 if num == 0 else num - 1
def moveL(num):
    return (num % 1000) * 10 + (num // 1000)
def moveR(num):
    return (num % 10) * 1000 + (num // 10)

operator = [
    (moveD, 'D'),
    (moveS, 'S'),
    (moveL, 'L'),
    (moveR, 'R')
]

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    start, target = map(int, sys.stdin.readline().split())
    visited = [False] * 10000
    queue = deque()
    queue.append((start, ""))

    found = False

    while queue:
        curr, path = queue.popleft()

        for method, char in operator:
            next_num = method(curr)
            if next_num == target:
                print(path+char)
                found = True
                break
            if not visited[next_num]:
                visited[next_num] = True
                queue.append((next_num, path+char))
        if found:
            break