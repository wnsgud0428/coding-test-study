def makeBest(times):
    MAX = 0
    for i in range(len(times)):
        temp = []
        temp.append(times[i])
        for j in range(i + 1, len(times)):
            if temp[-1][1] <= times[j][0]:
                temp.append(times[j])
        # print(temp)
        if len(temp) > MAX:
            MAX = len(temp)
        temp = []
    return MAX


N = int(input())
times = []
for i in range(N):
    times.append(tuple(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))
# print(times)

best = []
best.append(times[0])
for i in range(1, len(times)):
    if best[-1][1] <= times[i][0]:
        best.append(times[i])

print(len(best))

# # to do: times를 정리먼저 해야하지 않을까?
# MAX = makeBest(times)
# print(MAX)
