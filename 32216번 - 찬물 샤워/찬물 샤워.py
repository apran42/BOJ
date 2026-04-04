#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 32216                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/32216                          #+#        #+#      #+#     #
#    Solved: 2026/04/04 22:00:07 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, k, t = map(int, input().split())

d = list(map(int, input().split()))
degrees = []
answer = 0

for i in range(n):
    if t < k:
        t = t + d[i] + abs(t-k)
    elif t > k:
        t = t + d[i] - abs(t-k)
    else:
        t += d[i]
    degrees.append(t)

for d in degrees:
    answer += abs(k-d)

print(answer)