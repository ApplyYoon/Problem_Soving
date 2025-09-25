import sys
input = sys.stdin.readline

n = int(input().strip())
memo = [-1 for _ in range(n+1)]
memo[0] = 0
memo[1] = 1

def fibonacci(n):
    if n == 0: return 0
    if n == 1: return  1

    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)

    return memo[n]

print(fibonacci(n))