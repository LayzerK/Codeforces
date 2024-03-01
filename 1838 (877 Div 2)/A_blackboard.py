import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    arr = list(map(int, input().strip().split()))

    arr.sort()
    if arr[0] < 0:
        print(arr[0])
    else:
        print(arr[-1])

for tc in range(int(input())):
    solve()