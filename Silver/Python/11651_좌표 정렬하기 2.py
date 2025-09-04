import sys

N = int(sys.stdin.readline())
position = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
# 특정값을 기준으로 정렬 -> list.sort(key=lambda x:(우선순위1, 우선순위2, ...('-'는 내림차순)))
position.sort(key=lambda x: (x[1], x[0]))
for res in position:
    print(res[0], res[1])