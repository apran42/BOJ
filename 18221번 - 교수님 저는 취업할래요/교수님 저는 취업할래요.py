#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18221                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18221                          #+#        #+#      #+#     #
#    Solved: 2026/03/09 12:28:17 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def answer(input_data:list, pf:list, sk:list) ->None:
    student = 0
    row_dis = abs(pf[0]-sk[0])
    col_dis = abs(pf[1]-sk[1])
    row_start = min(pf[0], sk[0])
    col_start = min(pf[1], sk[1])

    if (pf[0]-sk[0])**2+(pf[1]-sk[1])**2 < 25:
        print(0)
        return
    for r in range(row_start, row_start+row_dis+1):
        for c in range(col_start, col_start+col_dis+1):
            student += 1 if input_data[r][c] == 1 else 0
    print(0 if student < 3 else 1)

n = int(input())

classroom = []
professor, seongkyu = [], []

for i in range(n):
    row = list(map(int, input().split()))
    if 5 in row:
        professor = [i, row.index(5)]
    if 2 in row:
        seongkyu = [i, row.index(2)]
    classroom.append(row)
answer(classroom, professor, seongkyu)