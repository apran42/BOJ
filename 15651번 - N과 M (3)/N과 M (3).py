#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15651                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15651                          #+#        #+#      #+#     #
#    Solved: 2026/04/15 00:41:09 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def backTracking(path:list):
    global answer
    if len(path) == length:     # 구하려는 길이에 도달
        answer.append(path[:])
        return
    
    for i in range(len(nums)):
        path.append(nums[i])
        backTracking(path)
        path.pop()

n, length = map(int, input().split())
nums = [i for i in range(1, n+1)]
answer = []
backTracking([])
for res in answer:
    print(*res)