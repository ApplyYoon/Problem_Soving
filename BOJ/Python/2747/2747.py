import sys
input = sys.stdin.readline
N = int(input().strip())
dp = [0 for i in range(N+1)]
dp[0], dp[1] = 0, 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])