N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# prefix sum 만들기
# (N+1) * (N+1) 선언 후, 0으로 다 채우기
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = (
            board[i - 1][j - 1]
            + prefix_sum[i - 1][j]
            + prefix_sum[i][j - 1]
            - prefix_sum[i - 1][j - 1]  # 겹치는 부분 빼주기
        )
# print(prefix_sum)


for _ in range(M):
    # 구간 합 구하기
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = (
        x1 - 1,
        y1 - 1,
        x2 - 1,
        y2 - 1,
    )  # 0부터 시작하는 index 값으로 맞추기

    interval_sum = (
        prefix_sum[x2 + 1][y2 + 1]
        - prefix_sum[x1][y2 + 1]
        - prefix_sum[x2 + 1][y1]
        + prefix_sum[x1][y1]
    )
    print(interval_sum)
