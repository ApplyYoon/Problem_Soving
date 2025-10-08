import sys
input = sys.stdin.readline

n = int(input())
mat = [tuple(map(int, input().split())) for _ in range(n)]

# 차원 배열 p
p = [mat[0][0]] + [c for (_, c) in mat]

dp = [[0] * n for _ in range(n)]

for length in range(2, n+1):  # 구간 길이
    for i in range(0, n-length+1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])