#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1337                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1337                           #+#        #+#      #+#     #
#    Solved: 2025/11/12 11:36:53 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))
num_list.sort()

diff = [] # 연속된 배열을 이루기에 부족한 수의 개수
for i in range(len(num_list)):
    curr = num_list[i] # 현재 수
    count = 0
    for j in range(i, len(num_list)):
        if num_list[j] < curr + 5: # 중복없고, 정렬되어있는 상태
            count += 1
        else: # 연속이 깨지면
            break
    diff.append(5-count) # 부족한 수 만큼
print(min(diff)) # 최솟