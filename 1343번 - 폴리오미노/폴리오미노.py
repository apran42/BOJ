#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1343                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1343                           #+#        #+#      #+#     #
#    Solved: 2026/03/27 17:02:19 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
board = input().replace('XXXX', 'AAAA').replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)