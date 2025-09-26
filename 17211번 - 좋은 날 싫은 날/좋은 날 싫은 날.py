#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17211                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17211                          #+#        #+#      #+#     #
#    Solved: 2025/09/26 11:59:38 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

# cond = 기분이 좋으면 0, 싫으면 1
n, cond = map(int, sys.stdin.readline().rstrip().split())

potential = {
    'good' : 0.0,
    'bad' : 0.0
}

line = sys.stdin.readline().rstrip()
good2good, good2bad, bad2good, bad2bad = map(float, line.split())
# 현재 기분이 좋음
if cond == 0:
    potential['good'] = good2good
    potential['bad'] = good2bad
# 현재 기분이 싫음
if cond == 1:
    potential['good'] = bad2good
    potential['bad'] = bad2bad

for _ in range(n-1): 
    tmp_good = (potential['good']*good2good + potential['bad']*bad2good)
    tmp_bad = (potential['good']*good2bad + potential['bad']*bad2bad)
    potential['good'] = tmp_good
    potential['bad'] = tmp_bad

sys.stdout.write(str(round(potential['good']*1000))+'\n')
sys.stdout.write(str(round(potential['bad']*1000)))