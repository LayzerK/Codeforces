import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def brute_solve():
  n = int(input())
  a = 0
  for i in range(2, n+1):
    sz = len(str(i)) - (i == pow(10, len(str(i))-1))
    #print(i, sz, normal_round(i, sz), chain_round(i, sz))
    if normal_round(i, sz) != chain_round(i, sz):
      #print(i, normal_round(i, sz), chain_round(i, sz))
      a += 1
  print(a)
  return a


def chain_round(n, sz):
  for i in range(1, sz+1):
    n = normal_round(n, i)
  return n


def solve():
  n = int(input())
  
  ans = 0
  str_n = str(n)
  for prefix in range(1, len(str_n)):
    start = int("4" * prefix + "5")
    end = int("5" + "0" * prefix)

    if n < int(start):
      break
    if n >= end:
      ans += end - start
    else:
      ans += n - start + 1
    
    
  print(ans)
  return ans


  


def normal_round(n, i):
  str_n = str(n)
  sz = len(str(n))
  #print("HERE", str_n[sz-i], str_n)
  if int(str_n[sz-i]) >= 5:
    str_n = str_n[:sz-i] + "0" * i
    n = int(str_n) + pow(10, i)
  else:
    str_n = str_n[:sz-i] + "0" * i
    n = int(str_n)
  return n
  



for tc in range(int(input())):
  solve()
    