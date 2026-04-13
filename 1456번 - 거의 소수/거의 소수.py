#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1456                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1456                           #+#        #+#      #+#     #
#    Solved: 2026/04/13 12:34:04 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

line = sys.stdin.readline()
a, b = map(int, line.split())

limit = int(b**0.5)
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False

count = 0

for p in range(2, limit + 1):
    if is_prime[p]:
        temp = p * p  
        
        while temp <= b:
            if temp >= a:
                count += 1
            if temp > b // p:
                break
            temp *= p

print(count)