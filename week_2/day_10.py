import sys


def play_game(row, col, N):
    row -= 1
    col -= 1

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[row][col] = True
    space = 1

    while True:
        count = int(board[row][col][:-1])
        command = board[row][col][-1]

        for _ in range(count):
            if command == 'L':
                col = col - 1 if col > 0 else N - 1
            elif command == 'R':
                col = (col + 1) % N
            elif command == 'U':
                row = row - 1 if row > 0 else N - 1
            else:
                row = (row + 1) % N

            if visited[row][col]:
                return space

            visited[row][col] = True
            space += 1

    return space


N = int(sys.stdin.readline().rstrip())

goorm = list(map(int, sys.stdin.readline().rstrip().split(" ")))
player = list(map(int, sys.stdin.readline().rstrip().split(" ")))

board = []

for _ in range(N):
    board.append(list(map(str, sys.stdin.readline().rstrip().split(" "))))

goorm = play_game(goorm[0], goorm[1], N)
player = play_game(player[0], player[1], N)

if goorm > player:
    print("goorm", goorm)
else:
    print("player", player)
