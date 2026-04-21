#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1865                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1865                           #+#        #+#      #+#     #
#    Solved: 2026/04/22 05:08:06 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n, m, wormHole = map(int, sys.stdin.readline().split())
    edges = []
    # 도로 정보
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    # 웜홀 정보
    for _ in range(wormHole):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, -t))

    # 벨만 - 포드 알고리즘
    dist = [0] * (n+1)
    dist[1] = 0

    has_neg_cycle = False
    for i in range(n):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t

                if i == n - 1:
                    has_neg_cycle = True
                    break
        if has_neg_cycle:
            break

    sys.stdout.write('YES\n' if has_neg_cycle else 'NO\n')