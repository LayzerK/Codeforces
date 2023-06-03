import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    arr = []

    inp = input().strip().split()
    
    for char in inp:
        if char[0] == "-":
            arr.append(-1*int(char[1:]))
        else:
            arr.append(int(char))

    small = (10**20)
    parity = 0
    ans = 0
    for n in arr:
        if n < 0:
            parity += 1
        
        small = min(small, abs(n))
        ans += abs(n)
    if parity%2:
        ans -= small * 2
    
    print(ans)
    
for tc in range(int(input())):
    solve()
