import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    n = int(input())
    s = input().strip()
    used = set()
    used.add(1)
    curr = 1
    mx = 1
    mn = 1
    left = 0

    while left < len(s):
        c = s[left]
        streak = 0
        while left < len(s) and c == s[left]:
            streak += 1
            left += 1
        
        for x in range(streak-1):
            if c == "<":
                curr +=1 
            else:
                curr -= 1
            used.add(curr)
        if c == ">":
            if curr > mn:
                curr = mn
            else:
                curr -= 1
        if c == "<":
            if curr < mx:
                curr = mx
            else:
                curr += 1

        mx = max(mx, curr)
        mn = min(mn, curr)
        used.add(curr)
    #print(used)
    print(len(used))
    #<<>>
    #1 < 2 < 3 > 2 > 1
        
        



    
for tc in range(int(input())):
    solve()
