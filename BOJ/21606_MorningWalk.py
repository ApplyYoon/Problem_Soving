import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input().strip())
input_places = input().strip()

graph = {i:[] for i in range(1, n+1)}
visited = [0 for i in range(n+1)]
places = [0]
cnt = 0

def DFS(start):
    global graph
    global visited
    global cnt

    # if places[start] == 1:
    #     cnt += 1
    #     return
    
    visited[start] = True
    for nxt in graph[start]:
        if not visited[nxt]:
            if places[nxt] == 1:
                cnt += 1
                continue
            DFS(nxt)

for _ in range(n-1):
    U, V = map(int, input().strip().split())
    graph[U].append(V)    
    graph[V].append(U)

for place in input_places:
    places.append(int(place))

sum = 0
idx = 0
print(graph)
print(places)
for place in places:
    visited = [0 for i in range(n+1)]
    if place == 1:
        cnt = 0
        DFS(idx)
        print(cnt)
        sum += cnt
    idx += 1
print(sum)