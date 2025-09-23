import sys

# 입력
n = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
sanggenu_cards = list(map(int, sys.stdin.readline().rstrip().split()))

is_have = [0]*m

for index, card in enumerate(sanggenu_cards):
    if card in cards:
        is_have[index] = 1

print(*is_have)