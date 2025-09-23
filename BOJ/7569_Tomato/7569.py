from collections import deque
import sys
input = sys.stdin.readline

N, M, H = map(int, input().strip().split())
board = [0 for _ in range(H)]
deq = deque()
for i in range(H):
    floor = []
    for __ in range(M):
        line = list(map(int, input().strip().split()))
        floor.append(line)
    board[i] = floor

def box_put():
    print("box")
    for i, floor in enumerate(board):
        print(i+1, '층')
        for line in floor:
            print(line)

is_in_zero = False
for z in range(H):
    for y in range(M):
        for x in range(N):
            if board[z][y][x] == 1:
                deq.append((z, y, x))
            elif board[z][y][x] == 0:
                is_in_zero = True

# print("deq")
# for elem in deq:
    # print(elem)

dx = [1, -1, 0, 0, 0, 0]   # → ←
dy = [0, 0, 1, -1, 0, 0]   # ↓ ↑
dz = [0, 0, 0, 0, 1, -1]   # 위, 아래

max_value = 0
while deq:
    z, y, x = deq.popleft()
    
    cur_board = board[z][y][x]
    for i in range(6):  # 여섯 방향
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        new_board = cur_board + 1
        if 0 <= nz < H and 0 <= ny < M and 0 <= nx < N:
            if board[nz][ny][nx] == 0:
                if new_board > max_value:
                    max_value = new_board
                board[nz][ny][nx] = new_board
                deq.append((nz, ny, nx))
# box_put()

is_full = True
for z in range(H):
    for y in range(M):
        for x in range(N):
            if board[z][y][x] == 0:
                is_full = False

if not is_full:
    print(-1)          
elif not is_in_zero:
    print(0)
else:
    print(max_value-1)

    # 정답처리만고치기