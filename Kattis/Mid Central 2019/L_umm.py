import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  s = input().strip().split()
  
  filtered = []
  for word in s:
    if all(c in "um" or not c.isalpha() for c in word):
      for c in word:
        if c in "um":
          filtered.append(c)

    
  output = []
  bit = 0
  for i, c in enumerate(reversed(filtered)):
    #print(i,c,bit)
    if c == "u":
      bit += 1 << ((i)%7)
    if (i+1)%7 == 0:
      output.append(chr(bit))
      bit = 0
  output = output[::-1]
  print("".join(output))

solve()
    