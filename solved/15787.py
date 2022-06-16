from collections import deque

N, M = map(int, input().split())
trains = [[]]
for i in range(N):
    trains.append([0 for j in range(20)])
# print(trains)

for cnt in range(M):
    info = list(map(int, input().split()))
    command, i = info[0], info[1]
    if command == 1:
        seat = info[2] - 1
        trains[i][seat] = 1
    elif command == 2:
        seat = info[2] - 1
        trains[i][seat] = 0
    elif command == 3:  # 뒤로 밀기
        deq_train = deque(trains[i])
        deq_train.pop()
        deq_train.appendleft(0)
        trains[i] = list(deq_train)
    elif command == 4:  # 앞으로 밀기
        deq_train = deque(trains[i])
        deq_train.popleft()
        deq_train.append(0)
        trains[i] = list(deq_train)

# print(trains)

trains_set = []
for i in range(1, N + 1):
    trains_set.append("".join(list(map(str, trains[i]))))

# print(trains_set)
print(len(set(trains_set)))
