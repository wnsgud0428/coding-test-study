N, M, R = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# print(N, M, R, arr)

for r in range(R):
    for i in range(min(N, M) // 2):
        temp = 0
        for j in range(i, N - 1 - i):
            next = arr[j + 1][i]
            if temp == 0:
                arr[j + 1][i] = arr[j][i]
            else:
                arr[j + 1][i] = temp
            temp = next
            # print(j, i)
        for j in range(i, M - 1 - i):
            next = arr[N - 1 - i][j + 1]
            arr[N - 1 - i][j + 1] = temp
            temp = next
            # print(N - 1 - i, j)
        for j in range(N - 1 - i, i, -1):
            next = arr[j - 1][M - 1 - i]
            arr[j - 1][M - 1 - i] = temp
            temp = next
            # print(j, M - 1 - i)
            # moveUp(j, M - 1 - i, arr, new_arr)
        for j in range(M - 1 - i, i, -1):
            next = arr[i][j - 1]
            arr[i][j - 1] = temp
            temp = next
            # print(i, j)
            # moveLeft(i, j, arr, new_arr)

    # print(r, arr)

# print(arr)


for l in arr:
    for e in l:
        print(e, end=" ")
    print()
