N = int(input())
events = []
max_col = 0
for i in range(N):
    a, b = map(int, input().split())
    events.append((a, b))
    if b > max_col:
        max_col = b
# print(max_col)
# print(N, events, max_col)
events.sort(key=lambda x: (x[0], -x[1]))

# print(events)

calendars = [[0 for i in range(max_col + 2)] for i in range(N + 1)]


def isThereEventsInPeriod(calendars, r, S, E):
    for i in range(S, E + 1):
        if calendars[r][i] != 0:  # 하나라도 0 아닌게 있으면 events가 있다고 true로 반환
            return True
    return False


def eventsInDay(calendars, day):
    max = 0
    for i in range(1, N + 1):
        if calendars[i][day] == 1:
            max = i
    return max


for e in events:
    r, S, E = 1, e[0], e[1]
    while isThereEventsInPeriod(calendars, r, S, E):
        r += 1
    for i in range(S, E + 1):
        calendars[r][i] = 1
# print(calendars)

sum = 0
height = 0
width = 0
for c in range(1, max_col + 2):  # 1~max_col
    events_count = eventsInDay(calendars, c)

    if events_count == 0:
        sum += height * width
        height, width = 0, 0
        continue

    if height < events_count:
        height = events_count
    if events_count > 0:
        width += 1
    # print(c, height, width, sum)

print(sum)
