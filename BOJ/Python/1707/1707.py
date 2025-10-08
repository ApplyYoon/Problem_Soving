import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

visited = []
color = []
graph = {}
success = True
def DFS(start, node_color):
    global visited
    global color
    global graph
    global success

    # 색이 같다면
    if color[start] != 0 and color[start] == node_color :
        success = False
        return

    if color[start] == 0:
        color[start] = node_color 
    visited[start] = True

    for nxt in graph[start]:
        if color[nxt] == node_color:
            success = False
        if not visited[nxt]:
            DFS(nxt, -node_color)

N = int(input().strip())
for _ in range(N):
    V, E = map(int, input().strip().split())
    visited = [0 for __ in range(V+1)]
    color = [0 for __ in range(V+1)]
    graph = {i:[] for i in range(1, V+1)}
    success = True
    for __ in range(E):
        node1, node2 = map(int, input().strip().split())
        graph[node1].append(node2)
        graph[node2].append(node1)


    # print(graph)
    for i in range(1, V+1):
        if not visited[i]:
            DFS(i, 1)
            
    if success:
        print("YES")
    else:
        print("NO")
    # print(color)
    # print(success)