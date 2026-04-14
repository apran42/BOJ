#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15649                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15649                          #+#        #+#      #+#     #
#    Solved: 2026/04/14 23:33:04 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def backTracking(path:list):
    global answer
    if len(path) == length:     # 구하려는 길이에 도달
        answer.append(path[:])
        return
    
    for i in range(len(nums)):
        if nums[i] in path:     # 이미 포함되어있으면 넘어감
            continue
        path.append(nums[i])
        backTracking(path)
        path.pop()

n, length = map(int, input().split())
nums = [i for i in range(1, n+1)]
answer = []
backTracking([])
for res in answer:
    print(*res)