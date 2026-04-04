#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 27159                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/27159                          #+#        #+#      #+#     #
#    Solved: 2026/04/04 21:52:41 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
cards = list(map(int, input().split()))

bundles = [[cards[0]]]
current_card = cards[0]
answer = 0
for c in cards[1:]:
    if current_card + 1 == c:
        bundles[-1].append(c)
    else:
        bundles.append([c])
    current_card = c

for b in bundles:
    answer += b[0]
print(answer)