n, k = map(int, input().split())

dp = [0] * n
dp[0] = 1
MOD = 10**9 + 7
for starting in range(n):
    for nxt in range(starting+1, min(n, starting+k+1)):
        dp[nxt] += dp[starting]
        dp[nxt] = dp[nxt] % MOD
print(dp[-1])
