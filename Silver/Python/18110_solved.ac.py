import sys
from math import floor
# 문제: 18110.solved.ac
# 내용: 주어진 의견의 개수 n의 절사평균(30%, 상위/하위:n*0.15)

# 초기값 
n = int(sys.stdin.readline())
opinions = [int(sys.stdin.readline()) for _ in range(n)]

# 예외처리
if n == 0:
    print(0)
    exit()

# 정렬
opinions.sort()

# 절사평균 (실제 세상의 사사오입 구현)
cut = int(len(opinions)*0.15+0.5)

# 절사한 의견
cutted_opinions = opinions if n <= 3 else opinions[cut:n-cut:]

print(int(sum(cutted_opinions)/len(cutted_opinions)+0.5))