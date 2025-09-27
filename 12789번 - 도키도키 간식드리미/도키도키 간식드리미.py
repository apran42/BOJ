#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12789                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12789                          #+#        #+#      #+#     #
#    Solved: 2025/09/28 06:30:47 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

class stack:
    def __init__(self):
        self.array = []
    
    def add(self, b):
        self.array.append(b)
    
    def last(self):
        if len(self.array) != 0:
            return self.array[-1]
        else:
            return None
     
    def pop(self):
        if len(self.array) != 0:
            self.array.pop()
    
n = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().rstrip().split()))
target = 1
line = stack()

cond = True
while True:
    # 성공적으로 마무리
    if target == n+1:
        break
    if target != line.last() and target not in students:
        cond = False
        break
    # 본 라인 혹은 임시 라인에 값이 있으면
    if (len(students) > 0 and students[0] == target) or line.last() == target:
        if len(students) > 0 and students[0] == target:
            students = students[1:]
        else:
            line.pop()
        target += 1
    else:
        line.add(students[0])
        students = students[1:]
    
if cond:
    sys.stdout.write('Nice')
else:
    sys.stdout.write('Sad')
