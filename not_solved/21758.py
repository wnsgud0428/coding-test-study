N = int(input())
place = list(map(int, input().split()))
place_r = list(reversed(place))

ans = 0  # 최대가 되야함
### 2케이스 에서 최대 구하기
max_2 = place[1]
max_index_2 = 1
for i in range(len(place)):
    if i == 0 or i == len(place) - 1:
        continue
    if place[i] > max_2:
        max_2 = place[i]
        max_index_2 = i

# print(max_index_2)

# 첫시도
# hap = sum(place[1 : max_index_2 + 1]) + sum(place[max_index_2 : len(place) - 2 + 1])
hap = sum(place[1 : len(place) - 2 + 1]) + max(place[1 : len(place) - 2 + 1])
# min_index_2_r = len(place) - 1 - max_index_2
# for i in range(max_index_2 + 1):  # 0 ~ temp_min_index
#     if i == 0:
#         continue
#     hap += place[i]
# for i in range(min_index_2_r + 1):  # 0 ~ temp_min_index_r
#     if i == 0:
#         continue
#     hap += place_r[i]

# print(hap)
ans = hap


### 1번 케이스
index = 1
hap = 0
for i in range(1, len(place) - 3 + 1):
    a = place[i]
    b = place[i + 1]
    if i + 1 == len(place) - 1:  # 요거 추가했으요
        break
    if not (a > 2 * b):
        index = i
        break
    pass

hap = sum(place[1:]) - place[i] + sum(place[i + 1 :])
# print("hap", hap)
if hap > ans:
    ans = hap

### 1`번 케이스(1번 케이스 역순)
index = 1
hap = 0
for i in range(1, len(place_r) - 3 + 1):
    a = place_r[i]
    b = place_r[i + 1]
    if i + 1 == len(place) - 1:
        break
    if not (a > 2 * b):
        index = i
        break
    pass

hap = sum(place_r[1:]) - place_r[i] + sum(place_r[i + 1 :])
# print("hap", hap)
if hap > ans:
    ans = hap

print(ans)
