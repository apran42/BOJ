#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 33883                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/33883                          #+#        #+#      #+#     #
#    Solved: 2025/10/10 11:07:07 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
output = sys.stdout.write

string = input().rstrip()
moeum = set(
    ['a','e','i','o','u']
)
jaeum_not_ns = set(
    ['b','c','d','f','g','h','j','k','l','m','p'
     ,'q','r','t','v','w','x','y','z']
)
moeum_in_string = []
for index, char in enumerate(string):
    if char in moeum:
        moeum_in_string.append(index)

if string[-1] in jaeum_not_ns:
    index = len(moeum_in_string)-1
    if index < 0:
        output('-1')
    else:
        output(str(moeum_in_string[index] + 1))
elif (string[-1] in moeum) or (string[-1] == 'n') or (string[-1] == 's'):
    index = len(moeum_in_string)-2
    if index < 0:
        output('-1')
    else:
        output(str(moeum_in_string[index] + 1))