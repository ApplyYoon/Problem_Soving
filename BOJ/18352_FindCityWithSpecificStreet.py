import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)

start = X

deq = deque()
deq.append(start)

dist = [-1] * (N+1)
dist[start] = 0

while deq:
    pop = deq.popleft()
    cur_dist = dist[pop]
    for nxt in graph[pop]:
        if dist[nxt] == -1:
            new_dist = cur_dist + 1
            dist[nxt] = new_dist            
            deq.append(nxt)

is_find = False
for i in range(len(dist)):
    if dist[i] == K:
        print(i)
        is_find = True
    
if not is_find:
    print("-1")