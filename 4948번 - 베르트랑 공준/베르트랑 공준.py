#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4948                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4948                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 11:45:57 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

def is_prime(n):
    root_n = int(n**0.5)+1

    for num in range(3, root_n, 2):
        if n%num == 0:
            return False
    return True


def count_primes_above_n(n):
    candidates=[]
    # n이 작은 경우의 예외처리. 현재 문제는 n초과여서 이렇게 함.
    if n == 1:
        candidates.append(2)
    if n == 2:
        candidates.append(3)
    # 시작 인덱스 
    start = max(n+1,5)
    candidates += [num for num in range(start, n*2+1) if (num%6 == 1 or num%6 == 5) and is_prime(num)]
    return len(candidates)


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    sys.stdout.write(str(count_primes_above_n(n))+'\n')