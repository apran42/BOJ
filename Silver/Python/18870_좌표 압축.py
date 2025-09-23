import sys

# sys.stdin = open('Silver\input.txt', 'r')

n = int(sys.stdin.readline())
# 원래 위치
real_position = list(map(int, sys.stdin.readline().rstrip().split()))

# 오름차순 정렬
nums = sorted(set(real_position))

zipped_postion = [0] * n

# 딕셔너리 형태
num_index = {num : index for index, num in enumerate(nums)}

for index in range(len(zipped_postion)):
    zipped_postion[index] = num_index[real_position[index]]

# element만 출력 
print(*zipped_postion)