#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30822                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30822                          #+#        #+#      #+#     #
#    Solved: 2026/04/16 10:07:58 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

length = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
uospc = [string.count(char) for char in 'uospc']
sys.stdout.write(str(min(uospc)))