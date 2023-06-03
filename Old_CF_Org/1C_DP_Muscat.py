n = int(input())
MOD = 10**9 + 7


dp = [[0, 0] for x in range(n+1)]

dp[0][0] = 1
dp[0][1] = 1
dp[1][0] = 1
dp[1][1] = 1

for nxt in range(2, n+1):
    dp[nxt][1] += dp[nxt-1][0]
    dp[nxt][1] += dp[nxt-2][0]
    dp[nxt][0] += dp[nxt-1][1]
    dp[nxt][0] += dp[nxt-1][0]

    dp[nxt][1] %= MOD
    dp[nxt][0] %= MOD
print(sum(dp[-1]) % MOD)
