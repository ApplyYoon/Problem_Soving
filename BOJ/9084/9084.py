T = int(input())
for _ in range(T):
    n = int(input())   
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target+1)
    dp[0] = 1

    for c in coins:
        for i in range(c, target+1):
            dp[i] += dp[i-c]

    print(dp)
    print(dp[target])  