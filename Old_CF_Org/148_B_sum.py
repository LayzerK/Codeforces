import sys
input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))
    arr.sort()
    l1 = 0
    l2 = 1

    # print(arr)
    running = sum(arr[:len(arr)-k])

    ans = running
    # print(ans)

    # start having assumed we removed all bigs, now go back and remove l1, l2 and add back in big
    # print(arr)
    for op in range(k):

        running += arr[len(arr)-k+op] - arr[l1] - arr[l2]
        # print(running)
        l1 += 2
        l2 += 2
        ans = max(ans, running)
    print(ans)


for tc in range(int(input())):
    solve()
