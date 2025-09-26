#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17202                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17202                          #+#        #+#      #+#     #
#    Solved: 2025/09/26 11:09:57 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import itertools

def jaegui(nums:list) -> list:
    if len(nums) == 2:
        return nums
    tmp = [str((int(nums[n])+int(nums[n+1]))%10)
           for n in range(len(nums)-1)]
    nums = tmp
    return jaegui(nums)

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
# 초기 세팅
nums = list(itertools.chain.from_iterable(zip(a,b)))

print(''.join(jaegui(nums)))