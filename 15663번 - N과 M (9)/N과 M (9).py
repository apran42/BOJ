#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15663                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15663                          #+#        #+#      #+#     #
#    Solved: 2026/04/15 02:09:07 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def backTracking( path:list):
    if len(path) == length:     # 구하려는 길이에 도달
        print(*path)
    last = -1
    for i in range(len(nums)):
        if not visited[i] and nums[i] != last:
            visited[i] = True
            path.append(nums[i])
            last = nums[i]
            backTracking(path)
            path.pop()
            visited[i] = False

n, length = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * n

backTracking([])