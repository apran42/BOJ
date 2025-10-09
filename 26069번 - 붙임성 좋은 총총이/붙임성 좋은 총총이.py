#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 26069                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/26069                          #+#        #+#      #+#     #
#    Solved: 2025/10/08 05:52:01 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

# 만남 횟수
n = int(input())

log = [set()]
index = 0
for _ in range(n):
    # 만남은 a←→b
    person_a, person_b = input().rstrip().split()
    # 총총이를 만나면 그 연결관계는 끊어짐
    # (아래 두 경우는 총총이를 만난 경우)
    if person_a == 'ChongChong':
        log[index].add(person_b)
        index += 1
        log.append(set())
    elif person_b == 'ChongChong':
        log[index].add(person_a)
        index += 1
        log.append(set())
    else:
        # 초기의 경우
        if index == 0:
            log[index].add(person_a)
            log[index].add(person_b)
        # 이미 총총이를 만난 분기가 존재
        else:
            if person_a in log[index-1]:
                log[index].add(person_b)
            elif person_b in log[index-1]:
                log[index].add(person_a)
            else:
                log[index].add(person_a)
                log[index].add(person_b)

ans = 0
for counter in log:
    ans += len(counter)

sys.stdout.write(str(ans))