import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    n = int(input())
    impossible = {1, 2, 3, 4, 5, 6, 9}
    if n in impossible:
        print("NO")
        return
    
    print("YES")

    if n % 3 == 0:
        print(1, 4, n-5)
    else:
        print(1, 2, n-3)

for tc in range(int(input())):
    solve()
    