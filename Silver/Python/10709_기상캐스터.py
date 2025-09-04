import sys

H, W= map(int,sys.stdin.readline().split(' '))
JOI=[list(sys.stdin.readline().strip()) for _ in range(H)]
cond=[list(-1 for _ in range(W)) for _ in range(H)]

for i in range(H):
    checked=0
    for j in range(W):
        if JOI[i][j] == 'c':
            cond[i][j]=0
            checked=1
            continue
        if checked==1:
            cond[i][j]=cond[i][j-1]+1

for row_cond in cond:
    for area_cond in row_cond:
        print(area_cond,end=' ')
    print()    