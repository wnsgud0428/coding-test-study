from collections import deque


# Node 클래스 정의
class Node:
    def __init__(self, r, c):
        self.r = r
        self.c = c


# 방향 벡터 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start, board, N, visited):
    queue = deque([start])
    visited[start.r][start.c] = True
    print(f"({start.r}, {start.c})", end=" ")

    while queue:
        v = queue.popleft()
        for i in range(4):
            nr = v.r + dr[i]
            nc = v.c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    print(f"({nr}, {nc})", end=" ")
                    queue.append(Node(nr, nc))


def print_array(arr):
    print("=====arr=====")
    for row in arr:
        print(row)
    print("=============")


def main():
    N = int(input())
    board = []

    for _ in range(N):
        board.append(list(map(int, input().split())))

    print_array(board)

    visited = [[False] * N for _ in range(N)]

    bfs(Node(0, 0), board, N, visited)


if __name__ == "__main__":
    main()
