#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20920                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20920                          #+#        #+#      #+#     #
#    Solved: 2025/10/10 01:07:43 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
output = sys.stdout.write

n, m = map(int, input().split())
# 단어장
words = dict()

for _ in range(n):
    word = input().rstrip()
    # 조건에서 제시한 길이 이상의 단어
    if len(word) >= m:
        # 이미 등장한 단어
        if word in words:
            words[word] += 1
        # 처음 등장하는 단어
        else:
            words[word] = 1
# 정렬
words = dict(sorted(words.items(), key=lambda x:(
    # 등장횟수에 의해
    -x[1],
    # 단어의 길이에 의해
    -len(x[0]),
    # 단어 자체의 오름차순 정렬(사전순)
    x[0]
)))

for word in words.keys():
    output(word+'\n')