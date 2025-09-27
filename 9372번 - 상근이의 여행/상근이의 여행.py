#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9372                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9372                           #+#        #+#      #+#     #
#    Solved: 2025/09/26 15:15:04 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

# TC의 수
tc = int(sys.stdin.readline())

for _ in range(tc):
    nation, airplane = map(int, sys.stdin.readline().split())
    for route in range(airplane):
        a_airport, b_airport = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(nation-1)+'\n')
