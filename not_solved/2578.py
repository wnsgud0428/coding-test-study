board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
numbers = []
for _ in range(5):
    numbers.extend(list(map(int, input().split())))

# print(board)
# print(numbers)


def positionOfNumber(board, num):
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == num:
                return i, j


def isBingo(visited):
    count = 0
    # 가로줄 검사
    for r in range(5):
        if not (False in visited[r]):
            count += 1

    # 세로줄 검사
    for c in range(5):
        temp_list = [visited[r][c] for r in range(5)]
        if not (False in temp_list):
            count += 1

    ortho_list1 = [visited[i][i] for i in range(5)]
    if not (False in ortho_list1):
        count += 1

    ortho_list2 = [visited[4 - i][i] for i in range(5)]
    if not (False in ortho_list2):
        count += 1

    if count >= 3:
        return True
    else:
        return False


visited = [[False] * 5 for _ in range(5)]
for i, num in enumerate(numbers):
    r, c = positionOfNumber(board, num)
    visited[r][c] = True
    if isBingo(visited):
        print(i + 1)
        break
