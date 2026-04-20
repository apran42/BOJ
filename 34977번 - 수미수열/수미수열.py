#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 34977                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/34977                          #+#        #+#      #+#     #
#    Solved: 2026/04/20 09:29:38 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def is_sumi_seq(seq:list):
    for i in range(1, len(seq)//2+1):
        if seq[:i] == seq[len(seq)-i:]:
            return True
        
    return False

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

print('yes' if is_sumi_seq(l) else 'no')