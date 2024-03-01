import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    n = int(input())

    intervals = []

    for rank in range(1, n+1):
        lb, rb = multiple_ints()

        intervals.append((rank, lb, rb))
    
    filtered = []

    for rank, lb, rb in intervals:
        sz = rb-lb + 1

        if sz >= 3:
            filtered.append((rank, lb, rb))
        
    ans = 0

    intervals = filtered

    i = 0

    while i < len(intervals) - 2:
        low_rank = intervals[i][0]
        mid_rank = intervals[i][1]
        high_rank = intervals[i+2][0]

        low_lb = intervals[i][1]
        low_rb = intervals[i][2]


        hi_lb = intervals[i+2][1]
        hi_rb = intervals[i+2][2]

        if low_lb <= high_rank <= low_rb and hi_lb <= low_rank <= hi_rb:
            ans += 1
            i += 3
        else:
            i += 1
    print(ans)

    #print(filtered)

solve()