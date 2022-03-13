n = int(input())
bomb_arr = [["." for i in range(n)] for i in range(n)]
open_arr = [["." for i in range(n)] for i in range(n)]


def bombCopy(bomb_arr, result_arr):
    for i in range(n):
        for j in range(n):
            if bomb_arr[i][j] == "*":
                result_arr[i][j] = "*"


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def returnNearBombCount(x, y, bomb_arr):
    count = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if bomb_arr[nx][ny] == "*":
                count += 1
    return count


for i in range(n):
    bomb_arr[i] = list(input())
for i in range(n):
    open_arr[i] = list(input())

# print(bomb_arr)
# print(open_arr)

# print(returnNearBombCount(1, 3, bomb_arr))

result_arr = [["." for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if open_arr[i][j] == "x" and bomb_arr[i][j] == "*":
            # 지뢰 복사해서 result_arr에 넣기
            bombCopy(bomb_arr, result_arr)
        if open_arr[i][j] == "x":
            # 주변 지뢰 개수 파악해서 result_arr에 넣기
            if result_arr[i][j] != "*":
                result_arr[i][j] = returnNearBombCount(i, j, bomb_arr)

# print(result_arr)

for i in range(n):
    for j in range(n):
        print(result_arr[i][j], end="")
    print()
