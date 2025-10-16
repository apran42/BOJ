#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13416                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13416                          #+#        #+#      #+#     #
#    Solved: 2025/10/16 08:34:13 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    answer = 0
    m = int(sys.stdin.readline())
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        # 3가지 경우 중 가장 큰 수가 음수일 수도 있으므로 0과 비교
        profit = max(a,b,c, 0)
        answer += profit
    sys.stdout.write(str(answer)+'\n')