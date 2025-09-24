#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11478                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11478                          #+#        #+#      #+#     #
#    Solved: 2025/09/24 11:00:13 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

string = list(sys.stdin.readline().rstrip())

string_set = set()
for i in range(len(string)):
    for j in range(len(string)-i):
        string_set.add(''.join(string[j:j+i+1]))
        t=string[j:j+i]
        print(t)
sys.stdout.write(str(len(string_set)))