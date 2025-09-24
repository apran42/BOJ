#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1764                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1764                           #+#        #+#      #+#     #
#    Solved: 2025/09/24 10:12:03 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
answer = 0
# 초기값
cant_=set()
cant_see_hear=set()
# 길이가 긴 set에서 짧은 입력들을 검사
if n>=m:
    for _ in range(n):
        cant_.add(sys.stdin.readline().rstrip())
    for _ in range(m):
        name = sys.stdin.readline().rstrip()
        if name in cant_:
            answer += 1
            cant_see_hear.add(name)
else:
    for _ in range(m):
        cant_.add(sys.stdin.readline().rstrip())
    for _ in range(n):
        name = sys.stdin.readline().rstrip()
        if name in cant_:
            answer += 1
            cant_see_hear.add(name)
print(answer)
for csh in sorted(cant_see_hear):
    sys.stdout.write(csh+'\n')