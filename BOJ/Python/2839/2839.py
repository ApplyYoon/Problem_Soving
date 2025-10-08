import sys
input = sys.stdin.readline

N = int(input())
INF = 10**9

dp = [INF] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    # dp[1], dp[2] = skip = INF
    if i >= 3:
        # dp[3] = min(dp[3], dp[0] + 1) = 1
        # dp[6] = min(dp[6], dp[3] + 1) = 2
        # dp[9] = min(dp[9], dp[6] + 1) = 3
        
        # dp[7] = min(dp[7], dp[4] + 1)
        # dp[4] = min(dp[4], dp[1] + 1)
        # dp[1] = INF
        dp[i] = min(dp[i], dp[i-3] + 1)
    if i >= 5:
        # dp[8] = min(dp[8], dp[5] + 1) = 2
        # dp[5] = min(dp[5], dp[0] + 1) = 1
        dp[i] = min(dp[i], dp[i-5] + 1)

print(dp[N] if dp[N] != INF else -1)