#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1074                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1074                           #+#        #+#      #+#     #
#    Solved: 2026/04/05 00:57:40 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(10**6)

def recur(n, r, c):
    if n == 0:
        return 0

    half = 2**(n-1)
    area = half**2 # 각 사분면의 넓이

    # 1사분면
    if r < half and c < half:
        return recur(n-1, r, c)
    # 2사분면: 1사분면은 이미 봤음
    elif r < half and c >= half:
        return area + recur(n-1, r, c-half)
    # 3사분면: 1, 2사분면은 이미 봤음
    elif r >= half and c < half:
        return area*2 + recur(n-1, r-half, c)
    # 4사분면: 1, 2, 3사분면은 이미 봤음
    else:
        return area*3 +recur(n-1, r-half, c-half) 


n, r, c = map(int, input().split())
    
answer = recur(n, r, c)
print(answer)