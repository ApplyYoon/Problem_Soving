from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node, visited):
    visited[node] = True
    print(node, end=" ")
    for nxt in sorted(graph[node]):
        if not visited[nxt]:
            dfs(nxt, visited)

def bfs(start):
    global graph
    visited = [False] * (V+1)
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for nxt in sorted(graph[node]):
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

input = sys.stdin.readline
V, E, start_node = map(int, input().split())   # V = 정점 개수
graph = {i: [] for i in range(1, V+1)}

for i in range(E):
    input_ = list(map(int, input().strip().split()))
    parent = input_[0]
    child = input_[1]

    graph[parent].append(child)
    graph[child].append(parent)

# print(graph)
dfs(start_node, [False] * (V+1))
print()
bfs(start_node)