#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24511                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24511                          #+#        #+#      #+#     #
#    Solved: 2025/10/06 23:35:16 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from queue import Queue
from sys import stdin
input = stdin.readline

# 자료구조의 개수
n = int(input())

# 수열 A
seq_A = list(map(int, input().split()))

# 수열 B
seq_B = list(map(int, input().split()))

# 삽입할 수열의 길이 
m = int(input())
# 수열 C
seq_C = list(map(int, input().split()))

# 큐에 해당하는 자료구조일 경우에만 값을 저장, 하나의 큐로 압축
real_seq = Queue()
for index in range(len(seq_A)-1, -1, -1):
    if seq_A[index] == 0:
        real_seq.put(seq_B[index])

answer = []

for c in seq_C:
    real_seq.put(c)
    answer.append(real_seq.get())

print(*answer)