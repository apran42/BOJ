#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 34760                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/34760                          #+#        #+#      #+#     #
#    Solved: 2026/03/26 15:12:27 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
elephants = list(map(int, input().split()))
max_elep = max(elephants)
if max_elep == elephants[-1]:
    if elephants.count(max_elep) == 1:
        print(max_elep)
    else:
        print(max_elep+1)
else:
    print(max_elep+1)