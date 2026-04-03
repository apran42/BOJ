#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2630                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2630                           #+#        #+#      #+#     #
#    Solved: 2026/04/03 13:16:33 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(10**6)

paper, blue, white = [], 0, 0

def cut(x, y, n):
    global blue, white

    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                m = n // 2
                cut(x, y, m)          
                cut(x, y + m, m)       
                cut(x + m, y, m)       
                cut(x + m, y + m, m)   
                return

    if color == 0:
        white += 1
    else:
        blue += 1
            
n = int(input())

for _ in range(n):
    paper.append(list(map(int, input().split())))

cut(0, 0, n)
print(white)
print(blue)