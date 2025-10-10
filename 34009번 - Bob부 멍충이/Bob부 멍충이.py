#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 34009                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/34009                          #+#        #+#      #+#     #
#    Solved: 2025/10/10 13:37:46 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())

if n % 2 == 1:
    output('Bob')
    sys.exit()

nums = list(map(int, input().split()))
nums.sort(reverse=True)

alice, bob = nums[0], nums[1]
for i in range(2, n, 2):
    alice += nums[i]
    if i+1 < n:
        bob += nums[i+1]
    if bob > alice:
        output('Bob')
        exit()
output('Alice')