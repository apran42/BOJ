#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15666                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15666                          #+#        #+#      #+#     #
#    Solved: 2026/04/15 02:29:40 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def backTracking(start:int, path:list):
    if len(path) == length:     # 구하려는 길이에 도달
        print(*path)
        return
    last = -1
    for i in range(start, len(nums)):
        if nums[i] != last:
            path.append(nums[i])
            last = nums[i]
            backTracking(i, path)
            path.pop()

n, length = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

backTracking(0, [])