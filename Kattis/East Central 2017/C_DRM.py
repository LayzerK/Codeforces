import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  s = input().strip()
  n = len(s)
  LH = list(s[:n//2])
  RH = list(s[n//2:])
  
  l_val = sum(ord(c) - ord('A') for c in LH)
  r_val = sum(ord(c) - ord('A') for c in RH)
  
  for i in range(n//2):
    RH[i] = chr((ord(RH[i]) - ord('A') + r_val)%26 + ord('A'))
    LH[i] = chr((ord(LH[i]) - ord('A')*2 + l_val + ord(RH[i]))%26 + ord('A')) 
  #(RH)
  print("".join(LH))

  

solve()