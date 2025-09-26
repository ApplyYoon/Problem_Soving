import sys
input = sys.stdin.readline

coins = []
N, K = map(int, input().strip().split())
for _ in range(N):
    x = int(input().strip())
    coins.append(x)

cnt = 0
for i in range(len(coins)-1, -1, -1):
    while K - coins[i] >= 0:
        K -= coins[i]
        cnt += 1

print(cnt)