import sys

N = int(sys.stdin.readline().rstrip())

item = N//14
N %= 14

item += N//7
N %= 7

item += N

print(item)
