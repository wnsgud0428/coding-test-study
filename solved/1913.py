N = int(input())
search_num = int(input())
snails = [[0 for i in range(N)] for i in range(N)]
# print(snails)


def write(snails, cur, i):
    # print("cur", cur)
    # print("i", i)
    snails[cur[0]][cur[1]] = i


# 상,하,좌,우
# 0  1  2  3
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move(direction, cur):
    cur[0] = cur[0] + dr[direction]
    cur[1] = cur[1] + dc[direction]


cur = [int(N / 2), int(N / 2)]  # 행,열
write(snails, cur, 1)
num = 2
for i in range(2, (int(N / 2) + 1) + 1):  # 2~
    move(0, cur)
    write(snails, cur, num)
    num += 1
    for j in range((i - 1) * 2 - 1):
        move(3, cur)
        write(snails, cur, num)
        num += 1
    for j in range((i - 1) * 2):
        move(1, cur)
        write(snails, cur, num)
        num += 1
    for j in range((i - 1) * 2):
        move(2, cur)
        write(snails, cur, num)
        num += 1
    for j in range((i - 1) * 2):
        move(0, cur)
        write(snails, cur, num)
        num += 1

# print(snails)
for sn in snails:
    for s in sn:
        print(s, end=" ")
    print("")


def search(snails, search_num):
    i = 0
    for sn in snails:
        j = 0
        for s in sn:
            if s == search_num:
                return i + 1, j + 1
            j += 1
        i += 1


position = search(snails, search_num)
print(position[0], position[1])
