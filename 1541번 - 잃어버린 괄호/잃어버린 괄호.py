#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1541                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1541                           #+#        #+#      #+#     #
#    Solved: 2026/02/21 17:05:13 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
nums = input().split('-')

answer = 0
for i, part in enumerate(nums):
    numbers = map(int, part.split('+'))
    if i == 0:
        answer += sum(numbers)
    else:
        answer -= sum(numbers)
print(answer)