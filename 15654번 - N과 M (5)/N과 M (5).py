#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15654                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15654                          #+#        #+#      #+#     #
#    Solved: 2026/04/15 00:47:57 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def backTracking(path:list):
    global answer
    if len(path) == length:     # 구하려는 길이에 도달
        answer.append(path[:])
        return
    
    for i in range(len(nums)):
        if nums[i] in path:
            continue
        path.append(nums[i])
        backTracking(path)
        path.pop()

n, length = map(int, input().split())
nums = list(map(int, input().split()))
answer = []
backTracking([])
answer.sort()
for res in answer:
    print(*res)