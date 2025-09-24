#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1269                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1269                           #+#        #+#      #+#     #
#    Solved: 2025/09/24 10:33:52 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
set_a = set()
tmp_set_a = set()
set_b = set()
# 집합 입력
list_a = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(a):
    set_a.add(list_a[i])
    tmp_set_a.add(list_a[i])
list_b = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(b):
    set_b.add(list_b[i])
# 차집합
for num in set_b:
    if num in set_a:
        set_a.remove(num)
for num in tmp_set_a:
    if num in set_b:
        set_b.remove(num)
for num in set_a:
    set_b.add(num)
sys.stdout.write(str(len(set_b)))