import sys

input = sys.stdin.readline
n = int(input().strip())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else: 
    memo = [-1 for i in range(n+1)]
    memo[1] = 1%15746
    memo[2] = 2%15746

    for i in range(3, n+1):
        memo[i] = (memo[i-1] + memo[i-2])%15746

    print(memo[n])