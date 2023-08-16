import sys

T = int(sys.stdin.readline().rstrip())
result = 0

for _ in range(T):
    first, operator, second = map(str, sys.stdin.readline().split(" "))

    if operator == '+':
        result += int(first) + int(second)
    elif operator == '-':
        result += int(first) - int(second)
    elif operator == '/':
        result += int(first) // int(second)
    else:
        result += int(first) * int(second)

print(result)

