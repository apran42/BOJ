#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 27891                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/27891                          #+#        #+#      #+#     #
#    Solved: 2026/04/04 22:30:31 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
string = input()

first, second = ord(string[0]), ord(string[1])

if ord(string[1]) == first + 4 or ord(string[1]) == first - 22:
    print('KIS')
elif ord(string[1]) == first + 16 or ord(string[1]) == first - 10:
    print('BHA')
else:
    if ord(string[2]) == second + 3 or ord(string[2]) == second - 23:
        print('NLCS')
    else:
        print('SJA')