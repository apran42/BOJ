from sys import stdin

a, m = map(int, stdin.readline().split(' '))
x=0
while (a*x)%m != 1:
    x+=1
print(x)
