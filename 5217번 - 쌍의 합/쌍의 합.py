#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5217                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5217                           #+#        #+#      #+#     #
#    Solved: 2026/03/26 10:46:47 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
test_case = int(input())

for _ in range(test_case):
    num = int(input())
    print(f'Pairs for {num}: ', end='')
    if num%2 == 0:
        for n in range(1, num//2):
            if n == 1:
                print(n, num-n, end='')
            else:
                print(',', n, num-n, end='')
    else:
        for n in range(1, num//2+1):
            if n == 1:
                print(n, num-n, end='')
            else:
                print(',', n, num-n, end='')
    print()