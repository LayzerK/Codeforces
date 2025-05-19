import sys
input = sys.stdin.readline

def solve():
    n,k, forbid = map(int, input().strip().split())

    if n == 1 and forbid == 1:
        print("NO")
    elif k == 1 and forbid == 1:
        print("NO")
    else:
        if forbid != 1:
            print("YES")
            print(n)
            ans = [1] * n
            print(*ans)
        elif forbid == 1:
            if k == 2 and n%2 == 1:
                print("NO")
            else:
                print("YES")
                print(n//2)
                if n % 2 == 0:
                    ans = [2] * (n//2)
                else:
                    ans = [2] * (n//2 - 1) + [3]
                print(*ans)
for tc in range(int(input())):
    solve()