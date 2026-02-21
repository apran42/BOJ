#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2447                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2447                           #+#        #+#      #+#     #
#    Solved: 2025/10/24 14:40:49 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
print = sys.stdout.write

def drawing(grid, x, y, size):
    if size == 1:
        return

    new_size = size // 3

    center_x = x + new_size
    center_y = y + new_size
    
    for i in range(new_size):
        for j in range(new_size):
            grid[center_y+i][center_x+j] = ' '

    for row in range(3):
        for col in range(3):
            if row == 1 and col == 1:
                continue

            new_x = x + col * new_size
            new_y = y + row * new_size

            drawing(grid, new_x, new_y, new_size)

n = int(input())
star = [['*' for _ in range(n)] for _ in range(n)]
drawing(star, 0, 0, n )

for row in star:
    tmp = ''.join(row)
    print(tmp+'\n')