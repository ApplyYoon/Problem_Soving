import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().strip().split())

board = []
for _ in range(R):
    line = list(map(str, input().strip()))
    board.append(line)

deq = deque()
water_deq = deque()
for i in range(R):
    for j in range(C):
        if board[i][j] == 'D':
            # board[i][j] = 2
            board[i][j] = -1
            end = (i, j)
        elif board[i][j] == 'S':
            board[i][j] = 0
            deq.append((i, j))
        elif board[i][j] == '*':
            board[i][j] = -3
            water_deq.append((i, j))
        elif board[i][j] == 'X':
            board[i][j] = -2
        else:
            board[i][j] = -1

# for elem in board:
#     print(elem)

is_able = False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while deq:
    for _ in range(len(deq)):
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 물이 들어와서 값이 바뀐 경우
            if board[x][y] == -3:
                break

            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                # print('bxy',board[x][y])
                deq.append((nx, ny))

    # print("Before Water")
    # for elem in board:
    #     print(elem)
    # print()
    
    for _ in range(len(water_deq)):
        x, y = water_deq.popleft()
        for i in range(4):
            # print("water")
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if (nx, ny) != end and board[nx][ny] != -2 and board[nx][ny] != -3:
                    # print("water!")
                    board[nx][ny] = -3
                    water_deq.append((nx, ny))

    # print("After Water")
    # for elem in board:
    #     print(elem)
    # # print("!!!")
    # print()

    if board[end[0]][end[1]] != -1:
        is_able = True        
        break

    # print("EOC")
if not is_able:
    print("KAKTUS")
else:
    print(board[end[0]][end[1]])