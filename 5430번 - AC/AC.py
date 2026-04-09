#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5430                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5430                           #+#        #+#      #+#     #
#    Solved: 2026/04/06 13:40:44 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    command = list(input()) # 명령어
    num = int(sys.stdin.readline()) # 배열 개수
    nums = sys.stdin.readline().strip()[1:-1] # 실제 배열
    if nums:
        nums = deque(nums.split(','))
    else:
        nums = deque()
    
    is_reversed, is_error = False, False

    for cmd in command:
        if cmd == 'R':
            is_reversed = not is_reversed
        elif cmd ==  'D':
            if not nums:
                is_error = True
                break
            else:
                if is_reversed:
                    nums.pop()
                else:
                    nums.popleft()

    if is_error:
        sys.stdout.write('error\n')
    else:
        if is_reversed:
            nums.reverse()
        sys.stdout.write('['+','.join(nums)+']\n')