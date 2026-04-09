#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5675                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5675                           #+#        #+#      #+#     #
#    Solved: 2026/04/09 11:15:50 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
while True:
    try:
        degree = int(input())
        if degree == 0 or degree % 6 == 0:
            print('Y')
        else:
            print('N')
    except EOFError:
        break