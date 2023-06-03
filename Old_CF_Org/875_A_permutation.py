import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))

    #1 2 4 5 3
    #1 2 4 3 5

    output = []

    for num in arr:
        output.append(n+1-num)
    print(*output)
    



  
  
    
for tc in range(int(input())):
    solve()
