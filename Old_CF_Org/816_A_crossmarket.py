import sys
input = sys.stdin.readline

#if a node is before its parent than it is 1 + parent discovery. Otherwise, it is = to parent discovery.
def solve():
    n,m = map(int, input().strip().split())

    if n > m:
        n,m = m,n

    if n == m == 1:
        print(0)
        return
    
    ans = (n-1) + (m-1) + n

    print(ans)



  
  
    
for tc in range(int(input())):
    solve()