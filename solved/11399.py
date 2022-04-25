N = int(input())
times = list(map(int, input().split()))

times.sort()


sum = 0
for i in range(0, N):
    for j in range(0, i + 1):
        sum += times[j]

print(sum)
