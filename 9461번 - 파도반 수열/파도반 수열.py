#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9461                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9461                           #+#        #+#      #+#     #
#    Solved: 2025/11/06 14:01:44 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
tc = int(input())
pado = [1,1,1,2,2,3,4,5,7,9]
for _ in range(tc):
    n = int(input())
    for _ in range(len(pado), n):
        pado.append(pado[-2] + pado[-3])
    print(pado[n-1])