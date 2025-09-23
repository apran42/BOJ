import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = sys.stdin.readline().split()
    answer = ''
    # a, b의 길이가 동일한 경우 
    if len(a) == len(b):
        for index in range(len(a)):
            answer += str(int(a[index])*int(b[index]))

    else:
        diff = abs(len(a)-len(b))
        long, short = (a, b) if len(a) > len(b) else (b, a)

        for index in range(diff):
            answer += long[index]
        for index in range(diff, len(long)):
            answer += str(int(long[index])*int(short[index-diff]))

    print(1 if int(answer) == int(a) * int(b) else 0)