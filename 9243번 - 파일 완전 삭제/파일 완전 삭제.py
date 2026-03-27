#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9243                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9243                           #+#        #+#      #+#     #
#    Solved: 2026/03/26 11:10:27 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
time = int(input())
origin_bits = input()
deleted_bits = input()
if time%2 == 0:
    print('Deletion succeeded' if origin_bits == deleted_bits else 'Deletion failed')
else:
    for index, bit in enumerate(origin_bits):
        if bit == deleted_bits[index]:
            print('Deletion failed')
            exit()
    print('Deletion succeeded')