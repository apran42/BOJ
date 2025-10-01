#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28323                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28323                          #+#        #+#      #+#     #
#    Solved: 2025/10/01 15:27:01 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import combinations

def all_unique_combinations(arr):
    n = len(arr)
    result = []
    for r in range(1, n + 1):  # 1개부터 n개까지
        result.extend(combinations(arr, r))  # r개 뽑는 조합
    return result

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0
# 모든 조합
for comb in all_unique_combinations(numbers):
    comb = list(comb)
    flag = True
    for index in range(1, len(comb)):
        # 짝수가 나오면 
        if (comb[index] + comb[index-1]) % 2 == 0:
            flag = False
            break
    # 조합된 원소의 최댓값
    answer = max(answer, len(comb)) if flag else answer
sys.stdout.write(str(answer))    