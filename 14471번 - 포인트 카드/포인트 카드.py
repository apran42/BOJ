#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14471                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14471                          #+#        #+#      #+#     #
#    Solved: 2026/04/16 10:11:28 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
point_card = [list(map(int, input().split())) for _ in range(m)]
need_to_change = [n-good for good, _ in point_card]
need_to_change.sort()
answer = 0
for ntc in need_to_change[:m-1]:
    answer += ntc if ntc > 0 else 0
sys.stdout.write(str(answer))