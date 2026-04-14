#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11444                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11444                          #+#        #+#      #+#     #
#    Solved: 2026/04/15 03:13:41 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
memo = {0: 0, 1: 1, 2: 1}

MOD = 1000000007

def fibo_fast(n):
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        k = n // 2
        memo[n] = (fibo_fast(k) * (2 * fibo_fast(k+1) - fibo_fast(k))) % MOD
    else:
        k = (n + 1) // 2
        memo[n] = (fibo_fast(k)**2 + fibo_fast(k-1)**2) % MOD
        
    return memo[n]

print(fibo_fast(int(input())))