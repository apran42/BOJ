#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 26069                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/26069                          #+#        #+#      #+#     #
#    Solved: 2025/10/08 05:52:01 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

# 만남 횟수
n = int(input())

log = set()
log.add('ChongChong')
for i in range(n):
    # 만남은 a←→b
    person_a, person_b = input().rstrip().split()
    if person_a in log:
        log.add(person_b)
    if person_b in log:
        log.add(person_a)
sys.stdout.write(str(len(log)))