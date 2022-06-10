boards = []
for i in range(19):
    boards.append(list(map(int, input().split())))

# visited = [[0 for i in range(19)] for i in range(19)]
# print(visited)

winner = 0
position = (0, 0)
isFive = False
isLeftEndNone = False
isRightEndNone = False

for i in range(19):
    for j in range(19):
        # 수평,수직,대각선 5목

        ###수평
        try:
            if (
                boards[i][j] == 1
                and boards[i][j + 1] == 1
                and boards[i][j + 2] == 1
                and boards[i][j + 3] == 1
                and boards[i][j + 4] == 1
            ):
                isFive = True
        except IndexError:
            pass
        try:
            if boards[i][j - 1] == 0 or boards[i][j - 1] == 2:
                isLeftEndNone = True
        except IndexError:
            isLeftEndNone = True
        try:
            if boards[i][j + 5] == 0 or boards[i][j + 5] == 2:
                isRightEndNone = True
        except IndexError:
            isRightEndNone = True
        if isFive and isLeftEndNone and isRightEndNone:
            position = (i, j)
            winner = 1
            break
        isFive = False
        isLeftEndNone = False
        isRightEndNone = False
        #####
        try:
            if (
                boards[i][j] == 2
                and boards[i][j + 1] == 2
                and boards[i][j + 2] == 2
                and boards[i][j + 3] == 2
                and boards[i][j + 4] == 2
            ):
                isFive = True
        except IndexError:
            pass
        try:
            if boards[i][j - 1] == 0 or boards[i][j - 1] == 1:
                isLeftEndNone = True
        except IndexError:
            isLeftEndNone = True
        try:
            if boards[i][j + 5] == 0 or boards[i][j + 5] == 1:
                isRightEndNone = True
        except IndexError:
            isRightEndNone = True
        if isFive and isLeftEndNone and isRightEndNone:
            position = (i, j)
            winner = 2
            break
        isFive = False
        isLeftEndNone = False
        isRightEndNone = False

        ######

        ###수직
        try:
            if (
                boards[i][j] == 1
                and boards[i + 1][j] == 1
                and boards[i + 2][j] == 1
                and boards[i + 3][j] == 1
                and boards[i + 4][j] == 1
            ):
                isFive = True
        except IndexError:
            pass
        try:
            if boards[i - 1][j] == 0 or boards[i - 1][j] == 2:
                isLeftEndNone = True
        except IndexError:
            isLeftEndNone = True
        try:
            if boards[i + 5][j] == 0 or boards[i + 5][j] == 2:
                isRightEndNone = True
        except IndexError:
            isRightEndNone = True
        if isFive and isLeftEndNone and isRightEndNone:
            position = (i, j)
            winner = 2
            break
        isFive = False
        isLeftEndNone = False
        isRightEndNone = False

        try:
            if (
                boards[i][j] == 2
                and boards[i + 1][j] == 2
                and boards[i + 2][j] == 2
                and boards[i + 3][j] == 2
                and boards[i + 4][j] == 2
            ):
                isFive = True
        except IndexError:
            pass
        try:
            if boards[i - 1][j] == 0 or boards[i - 1][j] == 1:
                isLeftEndNone = True
        except IndexError:
            isLeftEndNone = True
        try:
            if boards[i + 5][j] == 0 or boards[i + 5][j] == 1:
                isRightEndNone = True
        except IndexError:
            isRightEndNone = True
        if isFive and isLeftEndNone and isRightEndNone:
            position = (i, j)
            winner = 2
            break
        isFive = False
        isLeftEndNone = False
        isRightEndNone = False
        ######

        ###대각
        try:
            if (
                boards[i][j] == 1
                and boards[i + 1][j + 1] == 1
                and boards[i + 2][j + 2] == 1
                and boards[i + 3][j + 3] == 1
                and boards[i + 4][j + 4] == 1
            ):
                isFive = True
        except IndexError:
            pass
        try:
            if boards[i - 1][j - 1] == 0 or boards[i - 1][j - 1] == 2:
                isLeftEndNone = True
        except IndexError:
            isLeftEndNone = True
        try:
            if boards[i + 5][j + 5] == 0 or boards[i + 5][j + 5] == 2:
                isRightEndNone = True
        except IndexError:
            isRightEndNone = True
        if isFive and isLeftEndNone and isRightEndNone:
            position = (i, j)
            winner = 1
            break
        isFive = False
        isLeftEndNone = False
        isRightEndNone = False

        try:
            if (
                boards[i][j] == 2
                and boards[i + 1][j + 1] == 2
                and boards[i + 2][j + 2] == 2
                and boards[i + 3][j + 3] == 2
                and boards[i + 4][j + 4] == 2
            ):
                isFive = True
        except IndexError:
            pass
        try:
            if boards[i - 1][j - 1] == 0 or boards[i - 1][j - 1] == 1:
                isLeftEndNone = True
        except IndexError:
            isLeftEndNone = True
        try:
            if boards[i + 5][j + 5] == 0 or boards[i + 5][j + 5] == 1:
                isRightEndNone = True
        except IndexError:
            isRightEndNone = True
        if isFive and isLeftEndNone and isRightEndNone:
            position = (i, j)
            winner = 2
            break
        isFive = False
        isLeftEndNone = False
        isRightEndNone = False

        ######

    if winner != 0:
        break

if winner == 0:
    print(winner)
else:
    print(winner)
    print(position[0] + 1, position[1] + 1)

##################################################
# global count
# count = 0


# def bfs(i, j):
#     global count
#     origin_node = boards[i][j]
#     if boards[i][j] == 0 or visited[i][j] == 1:
#         return -1
#     count += 1
#     visited[i][j] = 1
#     print("(%d,%d)" % (i, j))
#     print("count:", count)
#     # 위쪽부터 시계방향으로
#     # if 배열 안벗어나는 범위
#     try:
#         if boards[i][j + 1] == origin_node:  # 우
#             bfs(i, j + 1)
#     except IndexError:
#         pass

#     try:
#         if boards[i + 1][j + 1] == origin_node:  # 오른쪽 아래
#             bfs(i + 1, j + 1)
#     except IndexError:
#         pass

#     try:
#         if boards[i + 1][j] == origin_node:  # 하
#             bfs(i + 1, j)
#     except IndexError:
#         pass

#     return boards[i][j]


# for i in range(19):
#     for j in range(19):
#         winner = bfs(i, j)
#         if count == 5:
#             print(winner)
#         count = 0
