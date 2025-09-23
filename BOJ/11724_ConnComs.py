import sys
sys.setrecursionlimit(10 ** 6)

def dfs(start):
    global visited
    visited[start] = True
    
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(nxt)

input = sys.stdin.readline
N, M = map(int, input().split())
graph = {i:[] for i in range(1, N + 1)}
visited = [False] * (N + 1)

for i in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)