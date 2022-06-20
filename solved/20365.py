import math

N = int(input())
colors = input()

# print(N, colors)

cnt = 0
for i in range(N - 1):
    if colors[i] != colors[i + 1]:
        cnt += 1

print(math.ceil(cnt / 2) + 1)
