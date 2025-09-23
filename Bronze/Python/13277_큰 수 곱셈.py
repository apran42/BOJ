import sys

# 문제: 13277. 큰 수 곱셈
# 내용: 두 정수 A와 B의 곰셉 / A, B는 300,000자리 이하

a, b = sys.stdin.readline().split()
if a == '0' or b == '0':
    print(0)
else:
    print(int(a)*int(b))