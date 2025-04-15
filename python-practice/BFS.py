from collections import deque

# 방문 여부를 저장하는 리스트
visited = [False] * 9
# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(9)]
graph[1] = [2, 3, 8]
graph[2] = [1, 7]
graph[3] = [1, 4, 5]
graph[4] = [3, 5]
graph[5] = [3, 4]
graph[6] = [7]
graph[7] = [2, 6, 8]
graph[8] = [1, 7]


# BFS 함수 정의
def bfs(start):
    queue = deque([start])
    visited[start] = True
    print(start, end=" ")

    while queue:
        v = queue.popleft()
        for next_node in graph[v]:
            if not visited[next_node]:
                visited[next_node] = True
                print(next_node, end=" ")
                queue.append(next_node)


# BFS 실행
bfs(1)
