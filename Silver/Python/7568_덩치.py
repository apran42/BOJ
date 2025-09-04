import sys

N = int(sys.stdin.readline())
people = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
li=[]
# count의 숫자가 작을 수록 덩치가 큼
for std in people:
    count=0
    for i in range(len(people)):
        if std[0] < people[i][0] and std[1] < people[i][1]:
            count+=1
    li.append(count+1)
for result in li:
    print(result, end=' ')
