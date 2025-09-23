#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2890                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2890                           #+#        #+#      #+#     #
#    Solved: 2025/09/24 04:15:40 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

r, c = map(int, sys.stdin.readline().split())
satellite_map = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
rank = []
dis = [0]*9
for line in satellite_map:
    index = 1
    count = 0
    # 출발 지점에서 얼마나 떨어져 있는지
    while line[index] == '.':
        count+=1
        index+=1
    # 빈 레인이 아닌 경우
    if count != len(line)-2:
        # rank[int(line[index])-1]
        dis[int(line[index])-1] = (len(line)-5-count)
 
sorted_dis = list(set(sorted(dis)))
for d in dis:
    rank.append(sorted_dis.index(d)+1)
print(dis,'\n',sorted_dis)
print(rank)