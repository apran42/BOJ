#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15650                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15650                          #+#        #+#      #+#     #
#    Solved: 2026/04/15 00:27:42 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def backTracking(start:int, path:list):
    global answer
    if len(path) == length:     # 구하려는 길이에 도달
        answer.append(path[:])
        return
    
    for i in range(start, len(nums)):
        if nums[i] in path:     # 이미 포함되어있으면 넘어감
            continue
        path.append(nums[i])
        backTracking(i+1, path)
        path.pop()

n, length = map(int, input().split())
nums = [i for i in range(1, n+1)]
answer = []
backTracking(0, [])
for res in answer:
    print(*res)