S = int(input())


def sum(N):
    return (1 + N) * N / 2


i = 1
is_found_ans = False
while True:
    value = sum(i)
    if value > S:
        break
    elif value == S:
        is_found_ans = True
        break
    elif value < S:
        i += 1

if is_found_ans:
    print(i)
elif not is_found_ans:
    print(i - 1)
