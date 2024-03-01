import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from math import inf
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    n,d = multiple_ints()
    prices = list(multiple_ints())
    prefix = [0] * n
    prefix[0] = prices[0]

    for i in range(1, n):
        prefix[i] = prefix[i-1] + prices[i]

    def round(num):
        rem = num % 10
        if rem > 5:
            return num + 10-rem
        else:
          return num - rem
        

    memo = {}

    def dfs(rb, rem):
        
        cost = inf
        if rem == 0:
            left_excluded = 0 if lb == 0 else prefix[lb-1]
            return round(prefix[-1] - left_excluded)
        

        for lb in range(rb):
            avail = rem - 1
            for left_alloc in range(avail+1):
                left_side = dfs(lb, left_alloc)
                right_side = dfs()

                cost = min(cost, left_side + right_side)
        #print(cost, lb, rb, "here")
        memo[(lb,rem)] = cost
        return cost
    
    ans = dfs(0, n-1, d)
    print(ans)
solve()