import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())

    arr = [i for i in range(1, n+1)]

    total = sum(arr)

    rem = total % n
    arr[rem-1] += rem

    print(" ".join(map(str, arr)))
