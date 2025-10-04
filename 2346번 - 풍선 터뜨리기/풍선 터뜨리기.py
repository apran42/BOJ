#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1874                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1874                           #+#        #+#      #+#     #
#    Solved: 2025/10/02 13:11:27 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
papers = list(map(int, input().split()))

# (풍선 번호, 종이값) 튜플로 관리
balloons = [(i+1, papers[i]) for i in range(n)]

answer = []
index = 0

while balloons:
    num, move = balloons.pop(index)   # 풍선 터뜨리기
    answer.append(num)

    if not balloons:
        break

    if move > 0:
        # 오른쪽으로 이동: (현재 위치 + (move-1)) % 남은 풍선 개수
        index = (index + move - 1) % len(balloons)
    else:
        # 왼쪽으로 이동: (현재 위치 + move) % 남은 풍선 개수
        index = (index + move) % len(balloons)

print(*answer)
