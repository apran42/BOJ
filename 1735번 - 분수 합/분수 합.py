#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1735                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1735                           #+#        #+#      #+#     #
#    Solved: 2025/09/24 11:30:18 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def gcd(a,b):
	a, b = max(a,b), min(a,b)
	while a!=0 and b!=0:
		a, b = b, a%b
	return a

bunsu1 = [0, 0]
bunsu2 = [0, 0]
bunsu1[0], bunsu1[1] = map(int, sys.stdin.readline().split())
bunsu2[0], bunsu2[1] = map(int, sys.stdin.readline().split())
bunmo = bunsu1[1]*bunsu2[1]
bunja = bunsu1[0]*bunsu2[1] + bunsu1[1]*bunsu2[0]

gongyaksu = gcd(bunmo, bunja)
bunmo //= gongyaksu
bunja //= gongyaksu

print(bunja, bunmo)