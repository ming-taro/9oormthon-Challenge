import sys

N = int(sys.stdin.readline().rstrip())
ingredients = list(map(int, sys.stdin.readline().rstrip().split(" ")))

max_index = ingredients.index(max(ingredients))

for index in range(1, max_index + 1):
    if ingredients[index - 1] > ingredients[index]:
        print(0)
        exit(0)

for index in range(N - 1, max_index + 1, -1):
    if ingredients[index - 1] < ingredients[index]:
        print(0)
        exit(0)

print(sum(ingredients))
