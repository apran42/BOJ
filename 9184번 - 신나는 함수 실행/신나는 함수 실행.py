#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9184                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9184                           #+#        #+#      #+#     #
#    Solved: 2025/11/05 00:25:10 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
table = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for a in range(21):
    for b in range(21):
        for c in range(21):
            if a <= 0 or b <= 0 or c <= 0:
                table[a][b][c] = 1
            elif a < b < c:
                table[a][b][c] = (table[a][b][c-1] +
                table[a][b-1][c-1] - table[a][b-1][c])
            else:
                table[a][b][c] = (
                    table[a-1][b][c] + table[a-1][b-1][c] +
                    table[a-1][b][c-1] - table[a-1][b-1][c-1]
                )

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        print(f'w({a}, {b}, {c}) = {1}')
    elif a > 20 or b > 20 or c > 20:
        print(f'w({a}, {b}, {c}) = {table[20][20][20]}')
    else:
        print(f'w({a}, {b}, {c}) = {table[a][b][c]}')
