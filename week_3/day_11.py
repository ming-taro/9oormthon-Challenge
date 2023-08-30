import sys

N = int(sys.stdin.readline().rstrip())
A, B = map(int, sys.stdin.readline().rstrip().split(" "))

B_count = N // B
N %= B

A_count = N // A
N %= A

while N > 0 and B_count > 0:
    B_count -= 1
    N += B

    A_count += N // A
    N %= A

if N == 0:
    print(A_count + B_count)
else:
    print(-1)
