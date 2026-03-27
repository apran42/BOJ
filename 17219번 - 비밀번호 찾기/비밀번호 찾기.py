#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17219                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17219                          #+#        #+#      #+#     #
#    Solved: 2026/03/27 11:09:27 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

site_num, password_num = map(int, sys.stdin.readline().split())

site_and_password = dict()

for _ in range(site_num):
    site_name, password = sys.stdin.readline().split()
    site_and_password[site_name] = password
    
for _ in range(password_num):
    sys.stdout.write(site_and_password[sys.stdin.readline().strip()]+'\n')