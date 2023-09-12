import sys


def is_within_range(row, col):
    if row >= 0 and col >= 0 and row < N and col < N:
        return True
    return False


def draw_line(direction, row, col):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if direction == 'U':
        index = 0
        d_index = 0
    elif direction == 'D':
        index = 1
        d_index = 0
    elif direction == 'L':
        index = 2
        d_index = 1
    else:
        index = 3
        d_index = 1

    while is_within_range(row, col):
        board[row][col][d_index] += 1
        row += dx[index]
        col += dy[index]


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
board = [[[0, 0] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    y, x, d = map(str, sys.stdin.readline().rstrip().split(" "))

    draw_line(d, int(y) - 1, int(x) - 1)

result = 0

for row in range(N):
    for col in range(N):
        result += board[row][col][0]*board[row][col][1]

print(result)
