#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1629                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1629                           #+#        #+#      #+#     #
#    Solved: 2026/04/16 13:14:44 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

a, n, mod = map(int, sys.stdin.readline().split())
powers = []
current_power = a % mod

temp_n = n
while temp_n > 0:
    powers.append(current_power)
    current_power = (current_power * current_power) % mod
    temp_n //= 2

answer = 1
for i in range(len(powers)):
    if (n >> i) & 1:
        answer = (answer * powers[i]) % mod

print(answer)