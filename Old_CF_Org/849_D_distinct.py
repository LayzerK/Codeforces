import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    n = int(input())
    s = input().strip()

    left = set(s[0])
    right = Counter(s[1:])
    ans = len(left) + len(right)
    for split in range(1, n-1):
        right[s[split]] -= 1
        if right[s[split]] == 0:
            del right[s[split]]
        
        left.add(s[split])
        #print(split, left, right)
        ans = max(ans, len(left) + len(right))
    
    print(ans)

for tc in range(int(input())):
    solve()
