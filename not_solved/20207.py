N = int(input())
events = []
max = 0
for i in range(N):
    a, b = map(int, input().split())
    events.append((a, b))
    if b > max:
        max = b

print(N, events, max)
events.sort(key=lambda x: (x[0], -x[1]))

print(events)

calendars = [[0 for i in range(max + 1)] for i in range(N)]


def isThereEvents(calendars, r, S, E):
    for i in range(S, E + 1):
        if calendars[r][i] != 0:  # 하나라도 0 아닌게 있으면 events가 있다고 true로 반환
            return True
    return False


for e in events:
    r, S, E = 1, e[0], e[1]
    while isThereEvents(calendars, r, S, E):
        r += 1
