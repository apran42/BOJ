#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11070                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11070                          #+#        #+#      #+#     #
#    Solved: 2026/03/13 00:50:08 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
testCase = int(input())

for _ in range(testCase):
    teams, plays = map(int, input().split())
    wins = [[0 for _ in range(2)] for _ in range(teams+1)]
    for _ in range(plays):
        teamA, teamB, teamAscore, teamBscore = map(int, input().split())
        wins[teamA][0] += teamAscore
        wins[teamA][1] += teamBscore
        wins[teamB][0] += teamBscore
        wins[teamB][1] += teamAscore
    pythagoras = [int(((t[0]**2)/(t[0]**2+t[1]**2))*1000//1) if (t[0]**2 + t[1]**2) != 0 else 0 for t in wins]
    print(max(pythagoras[1:]))
    print(min(pythagoras[1:]))


