bingo_arr = [[0 for i in range(5)] for i in range(5)]
for i in range(5):
    bingo_arr[i] = list(map(int, input().split()))
# print(bingo_arr)

call_num_list = []
for i in range(5):
    call_num_list.extend(list(map(int, input().split())))
# print(call_num_list)

bingo_tf = [[False for i in range(5)] for i in range(5)]


def returnBingoIndex(bingo_arr, num):
    for i in range(5):
        for j in range(5):
            if bingo_arr[i][j] == num:
                return i, j


def countBingoLine(tf_arr):
    count = 0
    for j in range(5):
        sum = 0
        for i in range(5):
            sum += tf_arr[i][j]
        if sum == 5:
            count += 1

    for i in range(5):
        sum = 0
        for j in range(5):
            sum += tf_arr[i][j]
        if sum == 5:
            count += 1

    diag_sum_1 = 0
    for i in range(5):
        diag_sum_1 += tf_arr[i][i]
    if diag_sum_1 == 5:
        count += 1

    diag_sum_2 = 0
    for i in range(5):
        diag_sum_2 += tf_arr[4 - i][i]
    if diag_sum_2 == 5:
        count += 1

    return count


# print(returnBingoIndex(bingo_arr, 14))

for c_num in call_num_list:
    a, b = returnBingoIndex(bingo_arr, c_num)
    bingo_tf[a][b] = True
    if countBingoLine(bingo_tf) >= 3:
        print(call_num_list.index(c_num) + 1)
        break
