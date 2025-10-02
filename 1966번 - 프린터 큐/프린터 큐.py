#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1966                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1966                           #+#        #+#      #+#     #
#    Solved: 2025/10/02 12:22:35 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    answer = 0
    docs, target_index = map(int, input().split())
    index = [i for i in range(docs)]
    # length = docs
    file_queue = list(map(int, input().split()))
    while True:
        # queue의 최우선
        first = max(file_queue)
        # queue의 첫 원소값이 최우선원소와 다르면 맨 뒤로 옮김
        if file_queue[0] != first:
            file_queue.append(file_queue[0])
            index.append(index[0])
            file_queue.pop(0)
            index.pop(0)
        # 같으면 queue에서 제거, 횟수 추가
        elif file_queue[0] == first:
            file_queue.pop(0)
            cur = index.pop(0)
            answer += 1
            # 현재 queue의 파일 인덱스가 target 인덱스와 같으면 탈출
            if cur == target_index:
                break
    sys.stdout.write(str(answer)+'\n')