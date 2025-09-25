import sys
n = int(sys.stdin.readline().strip())
memo = [-1 for _ in range(n+1)]
memo[0], memo[1] = 0, 1

def fibonacci(n):
    if memo[n] == -1:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)

    return memo[n]

print(fibonacci(n))