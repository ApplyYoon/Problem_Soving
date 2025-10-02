import sys
input = sys.stdin.readline

T = int(input().strip())
dp = [0 for _ in range(12)]
dp[1], dp[2], dp[3] = 1, 2, 4

for k in range(T):
    n = int(input().strip())
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])