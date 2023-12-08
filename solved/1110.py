N = str(input())
start = N
if len(start) < 2:
    start = "0" + start

cycle = 0
for i in range(1000000):
    cycle += 1
    if len(N) < 2:
        N = "0" + N
    new_num = N[1] + str(int(N[0]) + int(N[1]))[-1]
    # print(new_num)
    N = new_num
    if new_num == start:
        break

print(cycle)
