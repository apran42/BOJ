#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 31832                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/31832                          #+#        #+#      #+#     #
#    Solved: 2025/10/16 08:37:47 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
output = sys.stdout.write

def check_string(string):
    # 길이 검사
    if len(string) > 10:
        return False
    # 문자가 하나라도 있는지 검사
    has_char  = False
    upper, lower = 0, 0
    # 대/소문자 검사
    for char in string:
        if 65 <= ord(char) <= 90:
            upper += 1
        elif 97 <= ord(char) <= 122:
            lower += 1
        # 숫자 검사(숫자가 아닌 문자가 하나라도 있으면 True)
        if not char.isdecimal():
            has_char = True
    if upper > lower or not has_char:
        return False
    return True

n = int(input())
for _ in range(n):
    string = input().rstrip()
    # 조건에 맞는 문자열은 단 하나이므로 찾으면 바로 출력 후 종료
    if check_string(string):
        output(string)
        break