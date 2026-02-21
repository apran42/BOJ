#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11576                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11576                          #+#        #+#      #+#     #
#    Solved: 2025/11/12 10:12:50 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# 미래와 정이의 진법
future_numeral_system, jeong_numeral_system = map(int, input().split())
# 자릿수
digit = int(input())
# 미래 진법으로 나타낸 수
future_nums = list(map(int, input().split()))
# 10진법으로 전환
decimal_num = 0
for f_n in future_nums:
    decimal_num += f_n*future_numeral_system**(digit-1)
    digit -= 1
# 정이의 진법으로 변환하기 위해 자릿수를 구함
digit = 0
while decimal_num > jeong_numeral_system**digit:
    digit+=1
# 정이의 진법으로 변환
jeong_nums = []
while digit > 0:
    if digit == 1:
        jeong_nums.append(decimal_num)
    if digit != 1:
        current_digit_num = decimal_num//jeong_numeral_system**(digit-1)  
        jeong_nums.append(current_digit_num)
        decimal_num -= current_digit_num*(jeong_numeral_system**(digit-1))
    digit -= 1
print(*jeong_nums)