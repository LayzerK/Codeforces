import sys
input = sys.stdin.readline

for tc in range(int(input())):
    m, n = map(int, input().split())
    if m > n:
        n, m = m, n
    arr = list(map(int, input().split()))
    arr.sort()

    big = arr[-1]
    big2 = arr[-2]
    small = arr[0]
    small2 = arr[1]

    # smalltopleft

    case1 = big * (m*(n-1)) + big2 * (m-1) - (small * (m*n-1))
    case2 = big * (m*n-1) - (small * m*(n-1)) - (small2 * (m-1))
    print(max(case1, case2))
