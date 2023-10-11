import sys
input = sys.stdin.readline
from collections import defaultdict
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    n,k,c = multiple_ints()
    taken = defaultdict(int)

    surplus = []
    ans = []
    for placement in range(n):
        teamID, school = multiple_ints()
        if len(ans) == k:
            break
        
        if taken[school] < c:
            taken[school] += 1
            ans.append((teamID, placement))
        else:
            surplus.append((teamID, placement))
    
    missing = k - len(ans)

    for i in range(missing):
        ans.append(surplus[i])
    ans.sort(key = lambda x:x[1])
    for teamID, placement in ans:
        print(teamID)
solve()

