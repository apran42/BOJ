#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1874                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1874                           #+#        #+#      #+#     #
#    Solved: 2025/10/02 13:11:27 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
# 구하려고 하는 수열
sequence = [int(input()) for _ in range(n)]
stack = []
# + or -
answer = []
num = 1
while num <= n+1:
    # stack이 쌓여 있고, 수열에 해당하는 값을 꺼낼 수 있을 때
    if stack and sequence[0] == stack[-1]:
        stack.pop()
        sequence.pop(0)
        answer.append('-')
        pass
    # stack이 비어있거나, 비어있지 않아도 값을 꺼낼 수 없을 때
    elif not stack or (stack and sequence[0] != stack[-1]):
        stack.append(num)
        answer.append('+')
        num += 1

# 성공적으로 마무리 되면
if len(stack) == 1 and stack[0] == n+1:
    for a in answer[:-1:]:
        sys.stdout.write(a+'\n')
# 그렇지 못 한 경우
else:
    sys.stdout.write('NO')
    