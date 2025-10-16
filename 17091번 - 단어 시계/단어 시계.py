#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17091                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17091                          #+#        #+#      #+#     #
#    Solved: 2025/10/16 08:47:43 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
output = sys.stdout.write

hour = int(input())
minute = int(input())

hour_dict = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve"
}
minute_dict = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "quarter", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen", 20: "twenty", 21: "twenty one", 22: "twenty two",
    23: "twenty three", 24: "twenty four", 25: "twenty five",
    26: "twenty six", 27: "twenty seven", 28: "twenty eight",
    29: "twenty nine", 30: "half", 45: "quarter"
    }
# 정각
if minute == 0:
    output(hour_dict[hour] + " o' clock")
    sys.exit(0)
# 30분 이하, 30분 초과 처리
output_str = minute_dict[minute] if minute <= 30 else minute_dict[60-minute]
if minute%15 != 0 and minute < 30:
    output_str += " minute" + ("s" if minute != 1 else "") + " past "
elif minute%15 != 0 and minute > 30:
    output_str += " minute" + ("s" if minute != 59 else "") + " to "
elif minute == 15 or minute == 30:
    output_str += " past "
elif minute == 45:
    output_str += " to "
# 시각 처리 
if minute <= 30:
    output_str += hour_dict[hour]
else:
    output_str += hour_dict[hour+1 if hour != 12 else 1]
output(output_str)
