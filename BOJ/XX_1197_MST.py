import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
parent = [i for i in range(V+1)]
result = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += c

print(result)