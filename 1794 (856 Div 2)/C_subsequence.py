import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))

    size = 0
    ans = []
    #basically as long as size is greater than the new denom we are adding, we add it. otherwise we shrink. Left pter is derived from size

    for right in range(n):
        while(size < right+1 and arr[right-size] >= size +1):
            size += 1
            #basically as long as our shit is greater than the new denom, we gooo
        ans.append(size)
    
    print(*ans)

for tc in range(int(input())):
    solve()