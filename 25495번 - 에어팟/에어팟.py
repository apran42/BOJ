#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25495                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25495                          #+#        #+#      #+#     #
#    Solved: 2026/04/03 14:13:43 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
count = int(input())
tries = list(map(int, input().split()))

usage_battery = 2
last_usage = 2
for t in range(1, len(tries)):
    lastPhone = tries[t-1]
    currentPhone = tries[t]
    # 이전에 연결한 것과 같은 핸드폰에 연결
    if currentPhone == lastPhone and usage_battery != 0:
        usage_battery += last_usage*2
        last_usage *= 2
    else:
        usage_battery += 2
        last_usage = 2

    # 100%를 넘기면 충전
    if usage_battery >= 100:
        usage_battery = 0
        last_usage = 2

print(usage_battery)

