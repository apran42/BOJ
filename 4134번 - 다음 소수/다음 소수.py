#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4134                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4134                           #+#        #+#      #+#     #
#    Solved: 2025/09/24 13:48:13 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n%2 == 0:
        return False
    root_n = int(n**0.5) + 1
    for num in range(3, root_n):
        if n%num == 0:
            return False
    return True

n = int(sys.stdin.readline())

for _ in range(n):
    a = int(sys.stdin.readline())
    while not is_prime(a):
        a+=1
    print(a)