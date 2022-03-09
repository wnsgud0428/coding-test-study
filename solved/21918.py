N, M = map(int, input().split())
s = list(map(int, input().split()))
# print(N,M,s)


def one(i, x, s):  # i번째 전구 상태 x로 변경
    s[i - 1] = x


def two(l, r, s):
    for i in range(l - 1, r):
        s[i] = int(not s[i])


def three(l, r, s):
    for i in range(l - 1, r):
        s[i] = 0


def four(l, r, s):
    for i in range(l - 1, r):
        s[i] = 1


for i in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        one(b, c, s)
    elif a == 2:
        two(b, c, s)
    elif a == 3:
        three(b, c, s)
    elif a == 4:
        four(b, c, s)

for e in s:
    print(e, end=" ")
