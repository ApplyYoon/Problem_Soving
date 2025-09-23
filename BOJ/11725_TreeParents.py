import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input().strip())

graph = {
    i: [] for i in range(1, n + 1)
}

parents = [0 for i in range(n + 1)]
visited = [False] * (n+1)

def DFS(start, before) -> None:
    global parents
    global visited
    visited[start] = True
    if start != 1:
        parents[start] = before
    
    for nxt in graph[start]:
        if not visited[nxt]:
            DFS(nxt, start)

    return

for i in range(n-1):
    U, V = list(map(int, input().strip().split()))
    graph[U].append(V)
    graph[V].append(U)

DFS(1, 0)
for i in range(2, n+1):
    print(parents[i])