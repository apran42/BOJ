#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10981                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10981                          #+#        #+#      #+#     #
#    Solved: 2026/04/04 22:53:22 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, k = map(int, input().split())

info = []

for _ in range(n):
    univ, team, solved, penalty = input().split()
    solved, penalty = int(solved), int(penalty)

    info.append([univ, team, solved, penalty])

info.sort(key=lambda x:(-x[-2],x[-1]))

passed_univ = set()

for univ, team, solved, penalty in info:
    if univ not in passed_univ:
        print(team)
        passed_univ.add(univ)
        k -= 1
    
    if k == 0:
        break