#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14915                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14915                          #+#        #+#      #+#     #
#    Solved: 2025/10/01 13:18:01 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

m, n = map(int, sys.stdin.readline().split())

answer = ''
while m > 0:
    digit = m%n
    if digit >= 10:
        answer = chr(digit+55) + answer
    else:
        answer = str(digit) + answer
    m//=n
# 수가 0인 코너 케이스
if answer == '':
    answer += '0'
sys.stdout.write(answer)