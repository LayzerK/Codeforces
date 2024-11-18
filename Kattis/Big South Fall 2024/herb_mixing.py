def multiple_ints():
    return map(int, input().strip().split())
green, red = multiple_ints()

dp = {}
mn = -(10**20)
def dfs(g, r):
    if g < 0 or r < 0:
        return mn
    
    if(g,r) in dp:
        return dp[(g,r)]
    
    if g == 0:
        return 0
    
    take3 = dfs(g-3, r) + 10    
    take2 = dfs(g-2, r) + 3
    take1 = dfs(g-1, r) + 1
    takeboth = dfs(g-1, r-1) + 10

    ans = max(take3, take2, take1, takeboth)
    dp[(g,r)] = ans

    return ans

ans = max(0, dfs(green, red))

print(ans)