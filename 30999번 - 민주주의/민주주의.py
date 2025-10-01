#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30999                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30999                          #+#        #+#      #+#     #
#    Solved: 2025/10/01 11:27:40 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n, m = map(int, sys.stdin.readline().split())
answer = 0

for _ in range(n):
    vote = sys.stdin.readline().rstrip()
    o, x = 0, 0
    for v in vote:
        if v == 'O':
            o+=1
        else:
            x+=1
        if o > m//2:
            answer += 1
            break
        if x > m//2:
            break

sys.stdout.write(str(answer))