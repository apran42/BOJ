#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 6500                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/6500                           #+#        #+#      #+#     #
#    Solved: 2025/09/26 01:30:18 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys


while True:
    n = sys.stdin.readline().rstrip()
    if n == '0': break
    if len(n)<4:
        n = '0'*(4-len(n)) + n
    random_num = [n]
    while int(n) != 0:
        # n의 제곱값(string) 
        n = str((int(n))**2)
        # n^2 정상화
        if len(n)<8:
            n = '0'*(8-len(n))+n
        n = n[2:6]
        if n in random_num:
            break
        else:
            random_num.append(n)
    sys.stdout.write(str(len(random_num))+'\n')