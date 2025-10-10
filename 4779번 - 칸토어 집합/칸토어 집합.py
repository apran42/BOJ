#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4779                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4779                           #+#        #+#      #+#     #
#    Solved: 2025/10/10 03:19:58 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
output = sys.stdout.write

def Cantor(line, start, length):
    # 종료 조건
    if length <= 1:
        return
    # 1/3한 길이
    std = length // 3

    # 시작점과 종료점
    mid_start = start + std
    mid_end = start + 2 * std
    
    for i in range(mid_start, mid_end):
        line[i] = ' '
    # 재귀 호출
    Cantor(line, start, std)
    Cantor(line, mid_end, std)

while True:
    try:
        n = int(input())
    except:
        break
    if n != '':
        string = ['-']*(3**int(n))
        Cantor(string, 0, len(string))
        output(''.join(string)+'\n')