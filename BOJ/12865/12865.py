import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]  # (W, V)

dp = [0] * (K+1)

for W, V in items:
    for w in range(K, W-1, -1):  # 거꾸로 순회
        dp[w] = max(dp[w], dp[w-W] + V)

print(dp[K])