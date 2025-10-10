#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 33674                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/33674                          #+#        #+#      #+#     #
#    Solved: 2025/10/10 12:10:17 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from math import ceil
import sys
input = sys.stdin.readline
output = sys.stdout.write

n, d, k = map(int, input().rstrip().split())
s = list(map(int, input().rstrip().split()))

# 최대로 버틸 수 있는 날
maximum = float('inf')

for si in s:
    # 별이 안 떨어짐
    if si == 0:
        continue
    else:
        maximum = min(maximum, k // si)
# 매일 청소해야 함
if maximum == 0:
    output(str(d-1))
else:
    clean = ceil(d / maximum)-1
    output(str(clean))