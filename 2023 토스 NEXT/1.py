def solution(s, N):
    answer = 0

    from_1_to_n = set([i for i in range(1, N + 1)])
    print(from_1_to_n)
    l = len(s)
    res = []
    for start in range(l - N + 1):
        # print(s[start:start+N])
        sub_string = list(s[start : start + N])
        list_sub_string = list(map(int, sub_string))
        set_sub_string = set(list_sub_string)
        print(set_sub_string)
        if len(from_1_to_n - set_sub_string) == 0:
            res.append(int("".join(sub_string)))
    print(res)

    if len(res) == 0:
        print(-1)
        return -1
    else:
        print(max(res))
        return max(res)
