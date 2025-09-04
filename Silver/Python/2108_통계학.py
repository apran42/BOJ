from collections import Counter
import sys

N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]
li.sort()


# 1번
def avg(li):
  return round(sum(li) / len(li))


# 2번
def mid(li):
  return li[len(li) // 2]


# 3번
def mode(li):
  cnt = Counter(li)
  tmp = max(cnt.values())
  modes = [c for c, f in cnt.items() if f == tmp]
  return modes[1] if len(modes) > 1 else modes[0]


# 4번
def ran(li):
  return max(li) - min(li)


print(avg(li))
print(mid(li))
print(mode(li))
print(ran(li))
