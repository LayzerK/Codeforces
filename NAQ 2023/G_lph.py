import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    n, lph = multiple_ints()

    total = lph * 5

    problems = []

    for p in range(n):
        length = int(input())

        problems.append(length)
    
    problems.sort()

    ans = 0

    for p in problems:
        if p > total:
            break
        total -= p
        ans += 1
    
    print(ans)


solve()