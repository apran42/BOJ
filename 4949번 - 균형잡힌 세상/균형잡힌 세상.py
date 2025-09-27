#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4949                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4949                           #+#        #+#      #+#     #
#    Solved: 2025/09/28 02:39:27 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

class Stack:
    def __init__(self):
        self.bracket = []
    # 괄호 추가
    def add(self, b):
        self.bracket.append(b)
    # 괄호 삭제
    def erase(self):
        if len(self.bracket) != 0:
            return self.bracket.pop()
        else:
            return None
    # 길이를 반환, 비었으면 True, 있으면 False    
    def is_empty(self):
        return len(self.bracket) == 0
    
while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    bracket = Stack()
    
    cond = True
    for char in string:
        # 여는 괄호 추가
        if char == '(' or char == '[':
            bracket.add(char)
        # 닫는 괄호일 경우에
        if char == ')':
            if bracket.erase() == '(':
                continue
            else:
                cond = False
                break
        if char == ']':
            if bracket.erase() == '[':
                continue
            else:
                cond = False
                break
    # 조건에 만족
    if bracket.is_empty() and cond == True:
        sys.stdout.write('yes\n')
    else:
        sys.stdout.write('no\n')