#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1654                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1654                           #+#        #+#      #+#     #
#    Solved: 2026/04/06 12:56:44 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

have_lan, need_lan = map(int, input().split())
cables = [int(input()) for _ in range(have_lan)]
low = 1
high = max(cables)
result = 0
while low <= high:
    mid = (low + high) // 2
    cutted_cable = 0
    for cable in cables:
        cutted_cable += cable // mid
    # 자른 케이블이 필요한 것보다 많거나 같으면
    if cutted_cable >= need_lan:
        result = mid
        low = mid + 1
    else:
        high = mid - 1
print(result)