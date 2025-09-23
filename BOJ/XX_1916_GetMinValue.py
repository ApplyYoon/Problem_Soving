import sys, heapq
input = sys.stdin.readline
city_cnt = int(input().strip())
bus_cnt = int(input().strip())

dist = [float('inf')] * (city_cnt+1)
graph = [[] for _ in range(city_cnt+1)]
for _ in range(bus_cnt):
    u, v, w = map(int, input().strip().split())
    graph[u].append((w, v))

start, end = map(int, input().strip().split())

dist[start] = 0

pq = []
heapq.heappush(pq, (0, start))

while pq:
    cur_dist, u = heapq.heappop(pq)
    if dist[u] < cur_dist:
        continue
    for w, v in graph[u]:
        new_dist = cur_dist + w
        if new_dist < dist[v]:
            dist[v] = new_dist
            heapq.heappush(pq, (new_dist, v))


# print(graph)
# print(dist)
print(dist[end])





'''
3
3
1 3 3
1 2 2
2 3 2
1 3
'''