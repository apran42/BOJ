#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2083                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2083                           #+#        #+#      #+#     #
#    Solved: 2026/04/02 13:26:25 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
while True:
    name, age, weight = input().split()
    if name == '#' and age == '0' and weight == '0':
        break
    if int(age) > 17 or int(weight) >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')