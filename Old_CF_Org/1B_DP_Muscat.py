rows, cols = map(int, input().split())
grid = [[0 for x in range(cols)] for x in range(rows)]
for row in range(rows):
    rowinfo = map(int, input().split())
    for col, coin in enumerate(rowinfo):
        grid[row][col] = coin
dp = [[-(10**15) for x in range(cols)] for x in range(rows)]
dp[0][0] = grid[0][0]
for row in range(rows):
    for col in range(cols):
        curr = grid[row][col]
        if row-1 >= 0:
            dp[row][col] = max(dp[row][col], dp[row-1][col] + curr)
        if col - 1 >= 0:
            dp[row][col] = max(dp[row][col], dp[row][col-1] + curr)
print(dp[-1][-1])

# print(dp)
