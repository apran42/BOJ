#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17626                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17626                          #+#        #+#      #+#     #
#    Solved: 2026/04/02 10:40:25 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

num = int(sys.stdin.readline())

if int(num**(0.5))**2 == num:
    sys.stdout.write('1')
    exit()

for i in range(1, int(num**(0.5))+1):
    if int((num - i*i)**0.5)**2 == (num - i*i):
        sys.stdout.write('2')
        exit()

while num%4 == 0:
    num //= 4
sys.stdout.write('4' if num%8 == 7 else '3')
