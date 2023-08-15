import sys

W, R = map(int, sys.stdin.readline().rstrip().split(" "))

RM = W*(1 + R/30)

print(int(RM*10//10))