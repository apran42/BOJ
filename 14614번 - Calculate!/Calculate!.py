#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14614                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14614                          #+#        #+#      #+#     #
#    Solved: 2025/10/16 08:35:13 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
output = sys.stdout.write

# XOR 연산은 두 수가 다를 때 1, 같을 때 0
# 즉, c가 홀수일 때만 a와 b의 XOR 연산 결과가 나오고, 짝수일 때는 a가 그대로 출력됨
a,b,c = map(int, input().split())
output(str(a^b if c%2 == 1 else a))