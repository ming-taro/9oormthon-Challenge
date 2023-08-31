import sys
from collections import deque


def is_within_range(row, col):
    if row < 0 or row >= N or col < 0 or col >= N:
        return False
    return True


def visit_home(row, col):
    visited[row][col] = True
    queue = deque([[row, col]])

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    while queue:
        row, col = queue.popleft()

        for index in range(4):
            next_row = row + dx[index]
            next_col = col + dy[index]

            if (is_within_range(next_row, next_col)
                and board[next_row][next_col] == 1
                and visited[next_row][next_col] == False):
                queue.append([next_row, next_col])
                visited[next_row][next_col] = True


N = int(sys.stdin.readline().rstrip())
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

visited = [[False for _ in range(N)] for _ in range(N)]
total = 0

for row in range(N):
    for col in range(N):
        if visited[row][col] == False and board[row][col] == 1:
            visit_home(row, col)
            total += 1

print(total)
