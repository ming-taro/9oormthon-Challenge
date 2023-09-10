import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

island = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
result = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    island[a].append(b)

for i in range(1, N + 1):
    if visited[i]:
        continue

    queue = deque([i])
    visited[i] = True
    result += 1

    while queue:
        current_island = queue.popleft()

        for island_to_visit in island[current_island]:
            if (visited[island_to_visit] == False
                    and current_island in island[island_to_visit]):
                queue.append(island_to_visit)
                visited[island_to_visit] = True

print(result)
