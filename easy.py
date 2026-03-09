n = int(input())
fibbo = [0, 1]
if n > 1:
    for i in range(n-1):
        fibbo.append(fibbo[-1]+fibbo[-2])
print(fibbo[-1])