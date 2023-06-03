import sys
input = sys.stdin.readline


def solve():
  s = input().strip()
  #if there is a 1 then some  ??? and 0 in between nxt 1 it doesn't matter what you put. If you  haven't seen any 1s yet, put 0

  seen = False
  ans = []
  for char in s:
    if char == "1":
      seen = True
      ans.append("1")
    elif char == "0":
       seen = False
       ans.append("0")
    else:
       ans.append(str(int(seen)))
 
  
  

  print("".join(ans))
   
        
        



    
for tc in range(int(input())):
    solve()
