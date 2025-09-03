n=list(input())
sum=0
flag=-1
for i in range(len(n)):
    if n[i] != '*':
        if i%2 == 0:
            sum+=int(n[i])
        else:
            sum+=int(n[i])*3
    else:
        flag=i
        continue
sum%=10
weight = 1 if flag%2 ==0 else 3

for j in range(10):
    if (sum+j*weight) % 10 == 0:
        print(j)