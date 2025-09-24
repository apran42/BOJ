#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1620                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1620                           #+#        #+#      #+#     #
#    Solved: 2025/09/24 09:43:01 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n, m = map(int, sys.stdin.readline().split())
pokemon = {}
reverse_pokemon = {}
# 포켓몬 딕셔너리 추가
for no in range(n):
    name = sys.stdin.readline().rstrip()
    pokemon[name] = no+1
    reverse_pokemon[no+1] = name
for _ in range(m):
    question = sys.stdin.readline().rstrip()
    if question.isdecimal():
        print(reverse_pokemon[int(question)])
    else:
        print(pokemon[question])
