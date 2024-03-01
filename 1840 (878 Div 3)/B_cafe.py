import sys
input = sys.stdin.readline

def solve():
    n,k = map(int, input().strip().split())

    print(min(n+1, pow(2, min(k, 30))))

      


        
        

for tc in range(int(input())):
    solve()