#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1032                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1032                           #+#        #+#      #+#     #
#    Solved: 2026/03/13 00:36:29 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
testCase = int(input())

answer = []

for i in range(testCase):
    file = list(input())
    if i == 0:
        answer = file
        continue
    for index, char in enumerate(file):
        if answer[index] != char:
            answer[index] = '?'
print(''.join(answer))