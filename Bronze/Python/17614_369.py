N = int(input())

clapSum = 0
for num in range(1, N+1):
    listNum = list(str(num))
    
    threeClap = listNum.count('3')
    sixClap = listNum.count('6')
    nineClap = listNum.count('9')

    clapSum += threeClap+sixClap+nineClap
print(clapSum)