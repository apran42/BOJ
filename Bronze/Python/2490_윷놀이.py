for i in range(3):
    li = list(map(int, input().split()))
    con = li.count(0)
    if con == 0:
        print('E')
    else:
        print(chr(64+con))