#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30676                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30676                          #+#        #+#      #+#     #
#    Solved: 2026/03/26 10:36:11 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
num = int(input())

if 620 <= num <= 780:
    print('Red')
    exit()
if 590 <= num < 620:
    print('Orange')
    exit()
if 570 <= num < 590:
    print('Yellow')
    exit()
if 495 <= num < 570:
    print('Green')
    exit()
if 450 <= num < 495:
    print('Blue')
    exit()
if 425 <= num < 450:
    print('Indigo')
    exit()
if 380 <= num < 425:
    print('Violet')
    exit()