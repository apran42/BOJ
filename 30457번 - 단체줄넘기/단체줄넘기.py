#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30457                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30457                          #+#        #+#      #+#     #
#    Solved: 2025/10/12 02:53:55 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
student = list(map(int, input().split()))
dict_student = dict()
for stu in student:
    if stu in dict_student:
        dict_student[stu] += 1
    else:
        dict_student[stu] = 1
answer = 0
for stu in list(dict_student.keys()):
    answer += dict_student.get(stu) if dict_student[stu] <= 2 else 2
print(answer)