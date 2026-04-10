#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5525                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5525                           #+#        #+#      #+#     #
#    Solved: 2026/04/10 13:16:34 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
string_length = int(input())
string = input()
answer = 0
count = 0
i = 0

while i < (string_length-2):
    if string[i:i+3] == 'IOI':
        count += 1
        i += 2

        if count == n:
            count -= 1
            answer += 1
    else:
        count = 0
        i += 1
print(answer)