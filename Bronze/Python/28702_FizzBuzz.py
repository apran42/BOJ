fz = ['FizzBuzz', 'Fizz', 'Buzz']
li = []
for i in range(3):
  li.append(input())
idx = -1
num = -1
for word in li:
  if word in fz:
    continue
  else:
    idx = li.index(word)
    num = int(word)
num += 3 - idx
if num % 3 == 0 and num % 5 == 0:
  print(fz[0])
elif num % 3 == 0:
  print(fz[1])
elif num % 5 == 0:
  print(fz[2])
else:
  print(num)
