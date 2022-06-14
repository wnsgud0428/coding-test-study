T = int(input())  # 테스트 케이스 개수
n = []
d = []
X = [[] for i in range(T)]


for i in range(T):
    a, b = map(int, input().split())
    n.append(a)
    d.append(b)
    for j in range(n[i]):
        X[i].append(list(map(int, input().split())))

# 상0,하1,좌2,우3 // 상우4, 하우5, 하좌6, 상좌7
dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]


def rotatePlus45(X, n):  # n*n배열

    new_X = [[0 for i in range(n)] for i in range(n)]
    mid = (n // 2, n // 2)
    for i in range(n // 2):
        new_X[mid[1] + dr[4] * (i + 1)][mid[0] + dc[4] * (i + 1)] = X[
            mid[1] + dr[0] * (i + 1)
        ][mid[0] + dc[0] * (i + 1)]

        new_X[mid[1] + dr[5] * (i + 1)][mid[0] + dc[5] * (i + 1)] = X[
            mid[1] + dr[3] * (i + 1)
        ][mid[0] + dc[3] * (i + 1)]

        new_X[mid[1] + dr[6] * (i + 1)][mid[0] + dc[6] * (i + 1)] = X[
            mid[1] + dr[1] * (i + 1)
        ][mid[0] + dc[1] * (i + 1)]

        new_X[mid[1] + dr[7] * (i + 1)][mid[0] + dc[7] * (i + 1)] = X[
            mid[1] + dr[2] * (i + 1)
        ][mid[0] + dc[2] * (i + 1)]

        # 대각선에 있던 것들
        new_X[mid[1] + dr[3] * (i + 1)][mid[0] + dc[3] * (i + 1)] = X[
            mid[1] + dr[4] * (i + 1)
        ][mid[0] + dc[4] * (i + 1)]

        new_X[mid[1] + dr[1] * (i + 1)][mid[0] + dc[1] * (i + 1)] = X[
            mid[1] + dr[5] * (i + 1)
        ][mid[0] + dc[5] * (i + 1)]

        new_X[mid[1] + dr[2] * (i + 1)][mid[0] + dc[2] * (i + 1)] = X[
            mid[1] + dr[6] * (i + 1)
        ][mid[0] + dc[6] * (i + 1)]

        new_X[mid[1] + dr[0] * (i + 1)][mid[0] + dc[0] * (i + 1)] = X[
            mid[1] + dr[7] * (i + 1)
        ][mid[0] + dc[7] * (i + 1)]
    for r in range(n):
        for c in range(n):
            if new_X[r][c] == 0:
                new_X[r][c] = X[r][c]
    # print("new_X", new_X)
    return new_X


# print(T, n, d, X, end="\n\n")
for i in range(T):
    if d[i] == 0 or abs(d[i]) == 360:
        pass
    elif d[i] > 0:
        rotate_number = d[i] // 45
        for j in range(rotate_number):
            X[i] = rotatePlus45(X[i], n[i])
    elif d[i] < 0:
        rotate_number = (360 - abs(d[i])) // 45
        for j in range(rotate_number):
            X[i] = rotatePlus45(X[i], n[i])


def printArr(X, n):
    for i in range(n):
        for j in range(n):
            print(X[i][j], end=" ")
        print()


for i in range(T):
    printArr(X[i], n[i])
