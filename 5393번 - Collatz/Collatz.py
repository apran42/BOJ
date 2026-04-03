#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5393                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5393                           #+#        #+#      #+#     #
#    Solved: 2026/04/03 13:51:15 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
test_case = int(input())

for _ in range(test_case):
    answer = 0
    collatz = int(input())

    count_in = (collatz+1) // 2
    boundary = (collatz-1) // 3

    count_out = ((collatz+1) // 2) - ((boundary+1)//2)
    print(count_in+count_out)
