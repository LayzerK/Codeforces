import sys
input = sys.stdin.readline

def solve():
    n,k = map(int, input().strip().split())
    fruits = list(map(int, input().strip().split()))
    heights = list(map(int, input().strip().split()))

    ans = 0

    left = 0
    curr = 0

    for right, val in enumerate(fruits):
        curr += val
        if right > left:
            if heights[right-1] % heights[right] != 0:
                left = right
                curr = val
        
        while curr > k:
            curr -= fruits[left]
            left += 1
        #print(right, left, curr)
        ans = max(ans, right-left+1)
    
    print(ans)

for tc in range(int(input())):
    solve()