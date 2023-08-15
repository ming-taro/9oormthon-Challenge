import sys

N = int(sys.stdin.readline().rstrip())
T, M = map(int, sys.stdin.readline().rstrip().split(" "))

current_time = T*60 + M

for _ in range(N):
	c = int(sys.stdin.readline().rstrip())
	current_time += c

hour = current_time // 60 % 24
minute = current_time % 60

print(hour, minute)