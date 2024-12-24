import sys
from itertools import groupby
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n, p = multiple_ints()
  t1v = 1
  t2v = 2
  t1 = input().strip()
  t2 = input().strip()

  t1_comp = []
  t2_comp = []

  seq = []
  beaker = []
  for char, g in groupby(t1):
    t1_comp.append((char, len(list(g))))
  for char, g in groupby(t2):
    t2_comp.append((char, len(list(g))))
  
  if t2[0] == t1[-1]:
    t1_comp, t2_comp = t2_comp, t1_comp
    t1v, t2v = t2v, t1v

  #t1 is always the smalller compressed one

  t1_base = t1_comp[0][0]
  #inherently we will have len(t1_comp) - 1 pours to do


  t2_top = t2_comp[-1][0]
  #print(t1_base, t2_top)
  #print(t1_comp, t2_comp)
  t1_pours = len(t1_comp) - 1
  for i in range(t1_pours):
    val, sz = t1_comp.pop()
    if val == t1_base == t2_top:
      seq.append((t1v, t2v))
    else:
      beaker.append((val, sz))
      seq.append((t1v, 3))
    
  #now we have to get all of t1_base out of t2_comp

  rb = len(t2_comp) - 1 if t2_comp[0][0] == t1_base else len(t2_comp) - 2
  for i in range(rb + 1):
    val, _ = t2_comp.pop()
    if val == t1_base:
      seq.append((t2v, t1v))
    else:
      beaker.append((val, _))
      seq.append((t2v, 3))
  

  beaker = [x[0] for x in beaker]
  beaker = [c for c, g in groupby(beaker)]
  while beaker:
    val = beaker.pop()
    if val == t1_base:
      seq.append((3, t1v))
    else:
      seq.append((3, t2v))
  
  print(len(seq))
  #print(seq)
  if p > 1:
    for start, end in seq:
      print(start, end)

for tc in range(int(input())):
  solve()
  



