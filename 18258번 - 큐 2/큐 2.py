#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18258                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: flyingdisc1 <boj.kr/u/flyingdisc1>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18258                          #+#        #+#      #+#     #
#    Solved: 2025/09/30 14:03:19 by flyingdisc1   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

class Queue:
    def __init__(self):
        self.queue = []
        self.front_idx = 0  # 큐의 맨 앞을 가리키는 인덱스
    
    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.front_idx == len(self.queue):
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(self.queue[self.front_idx])+'\n')
            self.front_idx += 1

    def size(self):
        sys.stdout.write(str(len(self.queue) - self.front_idx)+'\n')
    
    def empty(self):
        sys.stdout.write('1\n' if self.front_idx == len(self.queue) else '0\n')

    def front(self):
        if self.front_idx == len(self.queue):
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(self.queue[self.front_idx])+'\n')

    def back(self):
        if self.front_idx == len(self.queue):
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(self.queue[-1])+'\n')


n = int(sys.stdin.readline())
q = Queue()

for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == 'push':
        q.push(int(order[1]))
    elif order[0] == 'pop':
        q.pop()
    elif order[0] == 'size':
        q.size()
    elif order[0] == 'empty':
        q.empty()
    elif order[0] == 'front':
        q.front()
    elif order[0] == 'back':
        q.back()


        