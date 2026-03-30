#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 29732                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/29732                          #+#        #+#      #+#     #
#    Solved: 2026/03/27 16:16:34 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m, k = map(int, input().split())

people = list(input())
effected_people = [False for _ in range(n)]

for index, p in enumerate(people):
    if p == 'R':
        start = max(0, index - k)
        end = min(n - 1, index + k)
        
        for j in range(start, end + 1):
            effected_people[j] = True

print('Yes' if effected_people.count(True) <= m else 'No')    