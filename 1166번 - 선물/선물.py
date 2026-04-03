#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1166                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1166                           #+#        #+#      #+#     #
#    Solved: 2026/04/03 14:25:38 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
num, length, width, height = map(int, input().split())

low = 0
high = max(length, width, height)
for _ in range(100):
    mid = (low+high) / 2
    tmp = (length//mid) * (width//mid) * (height//mid)

    if tmp >= num:
        low = mid
    else:
        high = mid

print(low)
