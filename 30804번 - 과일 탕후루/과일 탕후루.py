#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30804                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30804                          #+#        #+#      #+#     #
#    Solved: 2026/04/10 15:16:19 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
fruit = int(input())
tanghuru = list(map(int, input().split()))

count = {}
left, max_len, kind = 0, 0, 0

for right in range(fruit):
    fruit_right = tanghuru[right]
    if fruit_right not in count or count[fruit_right] == 0:
        kind += 1
        count[fruit_right] = 1
    else:
        count[fruit_right] += 1

    while kind > 2:
        fruit_left = tanghuru[left]
        count[fruit_left] -= 1
        if count[fruit_left] == 0:
            kind -= 1
        left += 1
    
    max_len = max(max_len, right-left+1)

print(max_len)