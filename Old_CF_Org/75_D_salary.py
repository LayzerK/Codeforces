import sys
input = sys.stdin.readline


def solve():
    n,s = map(int, input().strip().split())
    half = n//2
    arr = []
    base = 10**20
    cap = 0
    for i in range(n):
        l,r = map(int, input().strip().split())
        base = min(base, l)
        cap = max(cap, r)
        arr.append((l,r))
    arr.sort(key = lambda x:x[1])

    def check(med):
        used = 0
        above = 0
        below = 0
        t = 0
        for l,r in arr:

            if l < med and below < half:
                used += l
                below += 1
                t += 1
            elif med <= r:
                used += med
                above += 1
                t += 1
            else:
                used += left
                above += 1
                t += 1
        print(t, used, med)
        return above > half and used <= s

    left = 10
    right = 0
    #2 + 10 + 52 +23 + 44 + 44+ 54 + 66 + 62
    while left <= right:
        mid = (left+right)//2

        if check(mid):
            left = mid + 1
        
        else:
            right = mid - 1
    print(arr)
    print(check(76))
                
        



    
for tc in range(int(input())):
    solve()
