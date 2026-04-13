#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14500                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14500                          #+#        #+#      #+#     #
#    Solved: 2026/04/14 00:21:40 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def rotate(shape):
    return sorted([(c, -r) for r, c in shape])

def flip(shape):
    return sorted([(r, -c) for r, c in shape])

def normalize(shape):
    # 가장 왼쪽 위 칸을 (0,0)으로
    min_r = min(r for r, c in shape)
    min_c = min(c for r, c in shape)
    return tuple(sorted([(r - min_r, c - min_c) for r, c in shape]))

# 기본 형태
straight_tetromino = [(0, 0), (0, 1), (0, 2), (0, 3)]   # -
square_tetromino = [(0, 0), (0, 1), (1, 0), (1, 1)]     # ㅁ
l_tetromino = [(0, 0), (1, 0), (2, 0), (2, 1)]          # L
skew_tetromino = [(0, 0), (1, 0), (1, 1), (2, 1)]       # Z
t_tetromino = [(0, 0), (0, 1), (0, 2), (1, 1)]          # T

# 모든 경우의 수
all_shape = set()
for shape in [straight_tetromino, square_tetromino, l_tetromino, skew_tetromino, t_tetromino]:
    curr_shape = shape
    all_shape.add(tuple(curr_shape))
    for _ in range(4):
        curr_shape = rotate(curr_shape)
        all_shape.add(normalize(curr_shape))
        flipped = flip(curr_shape)
        all_shape.add(normalize(flipped))
all_shape = list(all_shape)

n, m = map(int, sys.stdin.readline().split())
paper = []

for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

answer = float('-inf')

for i in range(n):
    for j in range(m):
        for shape in all_shape:
            temp = 0
            for di, dj in shape:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m: # paper 범위 안에 있으면
                    temp += paper[ni][nj]
                else:
                    temp = 0
                    break
            if temp > answer:
                answer = temp

print(answer)