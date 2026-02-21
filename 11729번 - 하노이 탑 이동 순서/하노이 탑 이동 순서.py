#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11729                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11729                          #+#        #+#      #+#     #
#    Solved: 2025/11/05 00:19:44 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
print = sys.stdout.write

def hanoi(n, start, to, temp):
    if n == 0:
        return
    hanoi(n-1, start, temp, to)
    print(f"{start} {to}\n")
    hanoi(n-1, temp, to, start)

n = int(input())
print(f'{2**n-1}\n')
hanoi(n, '1', '3', '2')