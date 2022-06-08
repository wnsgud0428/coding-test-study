N, K = map(int, input().split())  # N이 카드개수, K가 섞은 회수
S = list(map(int, input().split()))
D = list(map(int, input().split()))

new_S = [0 for i in range(N)]
for i in range(K):
    for j in range(N):
        new_S[D[j] - 1] = S[j]
    # print(i, new_S)
    S = new_S.copy()

for s in S:
    print(s, end=" ")
