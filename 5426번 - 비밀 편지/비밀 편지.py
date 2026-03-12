#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5426                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5426                           #+#        #+#      #+#     #
#    Solved: 2026/03/13 01:29:03 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
testCase = int(input())

for _ in range(testCase):
    encodedString = list(input().rstrip())
    num = int(len(encodedString)**(0.5))
    for i in range(num-1,-1,-1):
        for j in range(num):
            print(encodedString[i+num*j], end='')
    print()