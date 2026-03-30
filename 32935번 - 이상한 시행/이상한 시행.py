#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 32935                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/32935                          #+#        #+#      #+#     #
#    Solved: 2026/03/30 10:13:16 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
num = int(input())

nums = list(map(int, input().split()))

current_sum = sum(nums)

while True:
    min_element = min(nums)
    # 원소 중 최솟값이 -(수열의 합)보다 작으면
    # 최솟값을 -(수열의 합)으로 변경, 수열의 합 업데이트
    if min_element < -current_sum:
        nums[nums.index(min_element)] = -current_sum
        current_sum = -min_element
    else:
        break

print(current_sum)