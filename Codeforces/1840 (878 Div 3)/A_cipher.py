import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    s = input()

    ans = []

    left = 0

    right = 1

    while right < n:
        if s[left] == s[right]:
            ans.append(s[left])
            left = right + 1
            right += 2
        else:
            right += 1
    print("".join(ans))
        
        

for tc in range(int(input())):
    solve()