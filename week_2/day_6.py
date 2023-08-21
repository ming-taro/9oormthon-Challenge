import sys

N = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()
R = N - 2

sub_string_list = []
sub_string_set = set()

for i in range(1, R + 1):
    for j in range(1, R + 1):
        for k in range(1, R + 1):
            if i + j + k == N:
                sub_string_list.append([S[:i], S[i:i + j], S[i + j:]])
                sub_string_set.add(S[:i])
                sub_string_set.add(S[i:i + j])
                sub_string_set.add(S[i + j:])

sub_string_set = sorted(list(sub_string_set))
sub_string_dict = {}

for index in range(len(sub_string_set)):
    sub_string_dict[sub_string_set[index]] = index + 1

max_score = 0

for sub_string in sub_string_list:
    score = (sub_string_dict[sub_string[0]]
             + sub_string_dict[sub_string[1]]
             + sub_string_dict[sub_string[2]])

    if score > max_score:
        max_score = score

print(max_score)
