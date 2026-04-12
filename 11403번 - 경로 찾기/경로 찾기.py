#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11403                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11403                          #+#        #+#      #+#     #
#    Solved: 2026/04/12 09:56:30 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n = int(sys.stdin.readline())
adjacency_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for mid in range(n):
    for start in range(n):
        for end in range(n):
            if (adjacency_matrix[start][mid] and adjacency_matrix[mid][end]):
                adjacency_matrix[start][end] = 1

for line in adjacency_matrix:
    print(*line)