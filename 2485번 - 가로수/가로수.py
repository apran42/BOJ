#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2485                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2485                           #+#        #+#      #+#     #
#    Solved: 2025/09/24 12:01:18 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
def gcd(a,b):
	a, b = max(a,b), min(a,b)
	while a!=0 and b!=0:
		a, b = b, a%b
	return a
n = int(sys.stdin.readline())

#이미 설치된 가로수
tree = []
for _ in range(n):
    tree.append(int(sys.stdin.readline()))
diff = []
for index in range(1, n):
    diff.append(tree[index] - tree[index-1])
# diff의 최대공약수
GCD = gcd(diff[0], diff[1])
for index in range(2, len(diff)):
    GCD = gcd(GCD, diff[index])
#가로수의 합계
answer = 0
print(GCD)
for d in diff:
    answer += (d//GCD)-1 if d!= GCD else 0
print(diff)
sys.stdout.write(str(answer))