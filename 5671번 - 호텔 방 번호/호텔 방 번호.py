#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5671                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5671                           #+#        #+#      #+#     #
#    Solved: 2026/04/04 22:45:21 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
while True:
    try:
        start, end = map(int, input().split())
        rooms = 0
        for number in range(start, end+1):
            number = list(str(number))
            temp_number = set(number)
            if len(number) == len(temp_number):
                rooms += 1
        print(rooms)

    except EOFError:
        break