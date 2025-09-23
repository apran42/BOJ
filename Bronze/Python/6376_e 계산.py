def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n
print('n', 'e'+'\n'+'- -----------')
for n in range(10):
    approx_e = 0.0
    for m in range(n+1):
        approx_e += 1/factorial(m)
    if n < 2:
        print(n, round(approx_e))
    #이건 좀... 8일 경우에 마지막이 0...
    elif n == 8:
        print(n, str(round(approx_e, 9))+'0')
    else:
        print(n, round(approx_e, 9))