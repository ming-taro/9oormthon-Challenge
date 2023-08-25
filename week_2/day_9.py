import sys


def bomb(y, x, N):
    dy = [0, 0, 0, -1, 1]
    dx = [0, -1, 1, 0, 0]  # ←, →, ↑, ↓

    for index in range(5):
        row = y - 1 + dy[index]
        col = x - 1 + dx[index]

        if (row < 0 or row >= N or col < 0 or col >= N):
            continue

        if status[row][col] == '0':
            board[row][col] += 1
        elif status[row][col] == '@':
            board[row][col] += 2


N, K = map(int, sys.stdin.readline().rstrip().split(" "))

status = []
board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    status.append(list(map(str, sys.stdin.readline().rstrip().split(" "))))

for _ in range(K):
    y, x = map(int, sys.stdin.readline().rstrip().split(" "))
    bomb(y, x, N)

max_bomb = 0

for b in board:
    max_bomb = max(max_bomb, max(b))

print(max_bomb)
