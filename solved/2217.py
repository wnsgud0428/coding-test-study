N = int(input())
ropes = []
for i in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)
# print(ropes)

max_w = 0
i = 0
for r in ropes:
    i += 1
    new_max_w = r * i
    # if 새로운 중량이 더크면: 업데이트
    if new_max_w >= max_w:
        max_w = new_max_w
        # print("max_w:", max_w)
    # 작으면 stop
    else:  # new_max_w < max_w
        # print("끝낼께요")
        break


print(max_w)
