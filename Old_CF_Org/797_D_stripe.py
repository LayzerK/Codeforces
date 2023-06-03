import sys
input = sys.stdin.readline

def solve():
    n,k = map(int, input().strip().split())
    s = input().strip()
    left = 0
    cnt = 0
    ans = 10**20
    cost = 0

    for right, char in enumerate(s):
        if right-left + 1 > k:
            if s[left] == "W":
                cost -= 1
            cnt -= 1
            left += 1

        if char == "W":
            cost += 1
        cnt += 1
        if cnt == k:
            #print(cost, ans)
            ans = min(cost, ans)
    print(ans)

for tc in range(int(input())):
    solve()