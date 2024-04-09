import sys
print(66668)
sys.stdout.flush()
groups = [0 for x in range(100004)]
groups[0] = 1
groups[100000] = 1

guess = int(input())

while guess != -1:
  if guess % 3 == 0:
    groups[guess] = 1
    print(guess//3 * 2 + 1) 
  else:
    if guess % 3 == 1:
      pair = guess + 1
    else:
      pair = guess - 1
    
    
    if not groups[guess]:
      groups[pair] = 1
      print(-1)
    else:
      print((guess//3 + 1) * 2)
  sys.stdout.flush()
  guess = int(input())

a = 0
for i in range(100001):
  if groups[i] or i % 3 == 0:
    a += 1
    print(i)
    sys.stdout.flush()

  elif i % 3 == 1 and  groups[i+1] == 0:
    print(i)
    a += 1
    sys.stdout.flush()

