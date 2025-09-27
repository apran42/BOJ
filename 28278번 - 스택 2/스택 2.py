import sys

n = int(sys.stdin.readline())
stack = [] 

for _ in range(n):
    order = sys.stdin.readline().rstrip()
    
    if order[0] == '1':  # push
        stack.append(int(order.split()[1]))
    
    elif order[0] == '2':  # pop
        if not stack:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(stack.pop()) + '\n')
    
    elif order[0] == '3':  # size
        sys.stdout.write(str(len(stack)) + '\n')
    
    elif order[0] == '4':  # empty
        sys.stdout.write('1\n' if not stack else '0\n')
    
    elif order[0] == '5':  # top
        if not stack:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(stack[-1]) + '\n')
