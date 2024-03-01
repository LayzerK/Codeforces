import sys
input = sys.stdin.readline


def solve():
    x,k = map(int, input().strip().split())

    if x%k != 0:
        print(1)
        print(x)
        return
    print(2)
    print(x-k-1, k+1)



    
for tc in range(int(input())):
    solve()
