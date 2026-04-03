#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5637                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5637                           #+#        #+#      #+#     #
#    Solved: 2026/04/03 14:04:29 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

answer = ''
max_length = -1

for line in sys.stdin:
    
    words = line.split()
    if not words:
        continue
    
    stop_condition = False
    for word in words:
        if word == 'E-N-D':
            stop_condition = True
            break
        clean_word = "".join(char for char in word if char.isalnum() or char == '-')
        
        if len(clean_word) > max_length:
            max_length = len(clean_word)
            answer = clean_word
            
    if stop_condition:
        break

print(answer.lower())