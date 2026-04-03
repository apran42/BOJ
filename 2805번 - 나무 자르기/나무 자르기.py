#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2805                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2805                           #+#        #+#      #+#     #
#    Solved: 2026/04/03 14:42:41 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

tree, sang_geun_tree = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))
low, high = 0, max(trees)
cutted, answer = 0, 0
while low <= high:
    mid = (high + low) // 2
    cutted = 0
    for t in trees:
        if t > mid:
            cutted += t - mid
    if cutted >= sang_geun_tree:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)