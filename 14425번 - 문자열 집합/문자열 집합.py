#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14425                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14425                          #+#        #+#      #+#     #
#    Solved: 2025/09/24 05:03:28 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n, m = map(int, sys.stdin.readline().split())

strings = [sys.stdin.readline().rstrip() for _ in range(n)]
to_check_string = [sys.stdin.readline().rstrip() for _ in range(m)]

answer = 0
for tc_string in to_check_string:
    for string in strings:
        if tc_string == string:
            answer += 1

print(answer)