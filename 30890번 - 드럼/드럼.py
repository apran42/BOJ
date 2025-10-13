#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30890                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+     #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30890                          #+#        #+#      #+#     #
#    Solved: 2025/10/12 03:34:33 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 최대공약수(GCD) 계산 함수
def gcd(a, b):
    while b:
        a, b = b, a % b  # 유클리드 호제법
    return a

input = sys.stdin.readline

# 입력: left, right 박자 간격
left, right = map(int, input().split())

# 최소공배수(LCM) 계산: 한 주기 패턴이 반복되는 시점
lcm = (left * right) // gcd(left, right)

# 다음 동작 시점 초기화
# left_term, right_term: 각 손이 움직이는 간격
# max_count: 추가 반복을 위해 초기값 설정 (LCM 이하 조건과 무관하게 반복 가능)
left_term, right_term, max_count = left, right, max(left, right)

# 루프: 한 손이라도 LCM 이하이거나, max_count가 남아 있으면 계속 반복
while (left <= lcm or right <= lcm) or max_count > 0:
    # 현재 두 손의 다음 연주 시점을 비교하여 순서 결정
    if left > right:
        # 왼손이 늦게 움직였으므로 오른손이 먼저 연주
        sys.stdout.write('1')
        right += right_term  # 오른손 다음 시점 갱신
    elif left < right:
        # 오른손이 늦게 움직였으므로 왼손이 먼저 연주
        sys.stdout.write('2')
        left += left_term   # 왼손 다음 시점 갱신
    else:
        # 두 손이 동시에 움직이면 양손 연주
        sys.stdout.write('3')
        left += left_term
        right += right_term

    # max_count는 매 루프마다 감소
    # > 0이면 LCM 조건과 상관없이 루프를 계속 돌게 함
    max_count -= 1