#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25192                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25192                          #+#        #+#      #+#     #
#    Solved: 2025/10/08 05:32:27 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

# 채팅방의 로그 기록 수
n = int(input())

enter = -1
log = []
# ENTER 이후에 메시지를 남긴 인원(중복 X)
for _ in range(n):
    msg = input().rstrip()
    if msg == 'ENTER':
        enter += 1
        log.append(set())  
        continue
    log[enter].add(msg)

answer = 0
for l in log:
    answer += len(l)
print(answer)