import sys
from collections import deque

def BFS() -> int:
    queue = deque([(0, 0)])   # 시작점
    dist = [[0]*M for _ in range(N)]
    dist[0][0] = 1            # 시작점 거리 = 1

    # 네 방향 (상, 하, 좌, 우)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            # 범위 안에 있고, 길(1)이고, 아직 방문 안 했다면
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return dist

input = sys.stdin.readline
N, M = map(int, input().strip().split())

maze = []
for _ in range(N):
    line = list(map(int, input().strip()))
    maze.append(line)

answer = BFS()

print(answer[N-1][M-1])