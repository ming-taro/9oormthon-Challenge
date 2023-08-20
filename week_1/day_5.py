import sys


def cal_binary(number):
    number_of_one = 0

    while number >= 1:
        if number % 2 == 1:
            number_of_one += 1
        number //= 2

    return number_of_one


N, K = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))

for index in range(N):
    number_list[index] = [number_list[index], cal_binary(number_list[index])]

number_list.sort(key=lambda x: (-x[1], -x[0]))

print(number_list[K - 1][0])
