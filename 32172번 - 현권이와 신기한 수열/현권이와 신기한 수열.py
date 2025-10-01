#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 32172                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/32172                          #+#        #+#      #+#     #
#    Solved: 2025/10/01 23:59:36 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n = int(sys.stdin.readline())

nums = set()
# 초기값
nums.add(0)
num = 0
for i in range(1, n+1):
    # num 계산
    num = num - i
    if num < 0 or num in nums:
        num += i*2
    # nums에 num추가
    nums.add(num)
sys.stdout.write(str(num))