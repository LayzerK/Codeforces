import sys
input = sys.stdin.readline
import heapq
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  arr = list(multiple_ints())
  bans = list(multiple_ints())
  used = set()
  banned = set()
  avail = [(-x,i) for i,x in enumerate(arr)]
  heapq.heapify(avail)
  curr = 0
  ans = 0
  ans_used = 0

  for pick in range(1, n+1):
    new_ban = bans[pick-2]-1 if pick > 1 else -1
    banned.add(new_ban)
    
    if new_ban in used:
      used.remove(new_ban)
      curr -= arr[new_ban]
      while avail and avail[0][1] in banned:
        heapq.heappop(avail)
      if not avail:
        break
      new_val, new_i = heapq.heappop(avail)
      used.add(new_i)
      curr = len(used) * new_val * -1
    
    while avail and avail[0][1] in banned:
      heapq.heappop(avail)
    #print("here", avail)
    if not avail:
      break
    new_val, new_i = heapq.heappop(avail)
    used.add(new_i)
    curr = len(used) * new_val * -1
    #print(used, curr, avail, banned)
    if curr > ans:
      ans = curr
      ans_used = pick
  print(ans, ans_used)


for tc in range(int(input())):
  solve()
    