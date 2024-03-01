import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    amap = defaultdict(int)
    bmap = defaultdict(int)

    streak = 1
    for i,n in enumerate(a):
        if i != 0:
            if n == a[i-1]:
              streak += 1
            else:
              streak = 1
        amap[n] = max(streak, amap[n])
    streak = 1
    for i,n in enumerate(b):
        if i != 0:
            if n == b[i-1]:
              streak += 1
            else:
              streak = 1
        bmap[n] = max(streak, bmap[n])
    ans = 0 

    for num, freq in amap.items():
       ans = max(ans, freq + bmap[num])
    for num, freq in bmap.items():
       ans = max(ans, freq + amap[num])
    
    print(ans)


    



  
  
    
for tc in range(int(input())):
    solve()
