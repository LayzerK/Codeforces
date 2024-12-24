import sys
input = sys.stdin.readline
from random import randint
def multiple_ints():
  return map(int, input().strip().split())

def find_subs(arr):
  cPos = 0
  cNeg = 0

  pos = 0
  neg = 0


  for val in arr:
    cPos += val
    cNeg += val

    if cNeg > 0:
      cNeg = 0
    if cPos < 0:
      cPos = 0

    pos = max(pos, cPos)
    neg = min(neg, cNeg)

  return (pos, neg) 

def solve():
  n = int(input())
  arr = list(multiple_ints())

  bound = -1

  #all subarray sums not including the special element are bounded by the most pos/neg subarrays on the left, right side




  #subarray sums INCLUDING the special element are bounded by the most positive and most negative L,R extensions
  #this enables us to get to special + most positive extension and special - most negative extension (only if there is a negative extension)

  LHPos = 0
  LHNeg = 0

  RHPos = 0
  RHNeg = 0

  special = 0


  for i,val in enumerate(arr):
    if val != -1 and val != 1:
      bound = i
      special = val
      break
  
  curr = 0
  for i in range(bound-1, -1, -1):
    curr += arr[i]

    LHPos = max(LHPos, curr)
    LHNeg = min(LHNeg, curr)
  
  curr = 0
  for i in range(bound + 1, len(arr)):
    curr += arr[i]

    RHPos = max(RHPos, curr)
    RHNeg = min(RHNeg, curr)
  


  LPosSub, LNegSub = find_subs(arr[:bound])
  RPosSub, RNegSub = find_subs(arr[bound+1:])

  posStreak = max(LPosSub, RPosSub)
  negStreak = max(abs(LNegSub), abs(RNegSub))
  subs = set()

  for i in range(posStreak + 1):
    subs.add(i)
  for i in range(negStreak + 1):
    subs.add(-i)
  
  
  maxPos = LHPos + RHPos
  maxNeg = LHNeg + RHNeg

  

  lb = special + maxNeg
  rb = special + maxPos
  if bound != -1:
    for i in range(lb, rb+1):
      subs.add(i)
  
  subs = list(subs)

  subs.sort()
  #print(maxNeg, maxPos ,LHNeg, RHNeg)
  print(len(subs))
  print(*subs)

  return subs



def brute_force():
  n = randint(1, 1000)
  special = randint(2, 5000)

  spec_index = randint(0, n-1)

  arr = []

  for i in range(n):
    if i == spec_index:
      arr.append(special)
    else:
      dec = randint(1, 2)

      if dec == 1:
        arr.append(-1)
      else:
        arr.append(1)
  
  subs = {0}


  for i in range(n):
    curr = 0
    for j in range(i, n):
      curr += arr[j]
      subs.add(curr)
  
  subs = list(subs)
  subs.sort()

  s_ans = solve(n, arr)

  if s_ans != subs:
    print("HEEERE", arr, special, spec_index, arr[spec_index])
    print(s_ans, subs)

  return subs

for tc in range(int(input())): 
  solve()
  #for i in range(40):
    #brute_force()
    