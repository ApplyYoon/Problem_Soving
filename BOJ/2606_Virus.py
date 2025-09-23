import sys
sys.setrecursionlimit(10 ** 6)

def dfs(start):
    global visited
    visited[start] = True

    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(nxt)

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
graph = {i: [] for i in range(1, n+1)}
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)
cnt = 0
for rs in visited:
    if rs == True:
        cnt += 1
print(cnt-1)