#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17103                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17103                          #+#        #+#      #+#     #
#    Solved: 2025/09/25 12:40:51 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def Sieve_of_Eratosthenes(n):
    nums = [True]*(n+1)
    # 0, 1 != prime number 
    nums[0]=nums[1]=False

    for index in range(2, int(n**0.5)+1):
        # 소수이면
        if nums[index]:
            for mul in range(index*index, n+1, index):
                nums[mul] = False

    # 소수 리스트
    prime = [p for p, b in enumerate(nums) if b]
    return prime


n = int(sys.stdin.readline())
# 최대 TC 이하의 소수 집합
prime_under_TC = set(Sieve_of_Eratosthenes(1_000_000))

for _ in range(n):
    g = int(sys.stdin.readline())
    partition = 0
    
    # 쌍으로 존재하므로 절반만 검사
    for num in range(2, (g//2+1)):
        if num in prime_under_TC and (g-num) in prime_under_TC:
            partition += 1

    sys.stdout.writelines(str(partition)+'\n')
