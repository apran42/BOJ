#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1918                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1918                           #+#        #+#      #+#     #
#    Solved: 2026/04/22 04:46:44 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

string = sys.stdin.readline().rstrip()

stack = []
answer = ''

def get_priority(op):
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    if op == '(':
        return 0
    return -1

for char in string:
    if 'A' <= char <= 'Z':
        answer += char

    elif char == '(':
        stack.append(char)
   
    elif char == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop() # '(' 삭제
    
    else:
        while stack and get_priority(stack[-1]) >= get_priority(char):
            answer += stack.pop()
        stack.append(char)
                
while stack:
    answer += stack.pop()

sys.stdout.write(answer)