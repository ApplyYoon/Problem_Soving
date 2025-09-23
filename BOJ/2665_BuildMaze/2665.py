import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    line = list(map(int, input().strip()))
    board.append(line)

dist = [[-1 for col in range(N)] for row in range(N)]
deq = deque()
deq.appendleft((0, 0))  # start = (0, 0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist[0][0] = 0
while deq:
    x, y = deq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        cur_dist = dist[x][y]        
        new_dist = cur_dist + 1           # 현재에서 +1 증가한 dist 값
        if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
            if board[nx][ny] == 1:        # 가중치가 없을 때
                deq.appendleft((nx, ny))
                dist[nx][ny] = cur_dist
            else:                         # 가중치가 있을 때
                deq.append((nx, ny))
                dist[nx][ny] = new_dist   # dist 값 증가
                
# print(dist)
print(dist[N-1][N-1])