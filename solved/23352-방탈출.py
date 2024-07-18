# <문제 분석>
# 임의의 방에서 다른 방으로 이동할 때는 항상 두 방 사이의 최단 경로로 이동한다.
# 1번을 만족하는 경로 중 가장 긴 경로의 시작 방과 끝 방에 적힌 숫자의 합

# <생각>
# 모든 칸에 대해서 BFS
# 가장 긴 경로 길이 저장, 시작+끝 합 저장
# 길이순 정렬, 합 순 정렬


# BFS * 모든칸 ->  N*M * (N*M)
# 50^4 = 5^4 * 10^4 = 625 ^ 10^4 = 6.25 * 10^6

# <수도코드>
# 경로 길이, 시작+끝 값 담은 list
# for N:
#     for M:
#         BFS돌리기(return 긴 경로 길이, 시작+끝 값)
#         list에 append

# 길이순, 합 순 정렬


# <코드>
from collections import deque


class Node:
    def __init__(self, r, c):
        self.r = r
        self.c = c


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start_node, board):
    N, M = len(board), len(board[0])
    visited = [[False] * M for _ in range(N)]
    length = [[0] * M for _ in range(N)]

    q = deque()
    visited[start_node.r][start_node.c] = True
    q.append(start_node)

    while q:
        v = q.popleft()
        for i in range(4):
            nr = v.r + dr[i]
            nc = v.c + dc[i]
            if 0 <= nr <= N - 1 and 0 <= nc <= M - 1:
                if not visited[nr][nc] and board[nr][nc] != 0:
                    visited[nr][nc] = True
                    length[nr][nc] = length[v.r][v.c] + 1
                    q.append(Node(nr, nc))

    # 최대 경로가 여러개일수 있음
    max_length = -1
    for i in range(N):
        for j in range(M):
            max_length = max(length[i][j], max_length)

    max_length_end_node = []
    for i in range(N):
        for j in range(M):
            if length[i][j] == max_length:
                max_length_end_node.append(Node(i, j))

    max_end_node_value = -1
    for node in max_length_end_node:
        max_end_node_value = max(max_end_node_value, board[node.r][node.c])

    sum_start_to_end = board[start_node.r][start_node.c] + max_end_node_value

    return max_length, sum_start_to_end


save = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            length, hap = bfs(Node(i, j), board)
            save.append([length, hap])
save.sort(key=lambda x: (-x[0], -x[1]))
# print(save)


answer = None
if len(save) >= 1:
    answer = save[0][1]
else:
    answer = 0
print(answer)
