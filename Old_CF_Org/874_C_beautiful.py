import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    oddlow = 10**20
    arr = list(map(int, input().strip().split()))
    for num in arr:
        if num % 2:
            oddlow = min(oddlow, num)
    odd = True
    #you can never convert everything to evens, the lowest odd number you have will still need to be converted and that can never be converted
    even = True

    for num in arr:
        if num % 2:
            even = False
        else:
            if num < oddlow:
                odd = False
    if even or odd:
        print("YES")
    else:
        print("NO")

for tc in range(int(input())):
    solve() 