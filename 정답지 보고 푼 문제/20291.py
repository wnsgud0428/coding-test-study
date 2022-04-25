N = int(input())
exts = {}

for i in range(N):  # O(N)
    ext = input().split(".")[1]
    if ext in exts:
        exts[ext] += 1
    else:
        exts[ext] = 1

sorted_exts = sorted(exts.items())  # O(N*logN)

for ext in sorted_exts:  # O(N)
    print(ext[0], end=" ")
    print(ext[1])

# O(N*logN)


""" 처음짠 코드(시간 초과남)
N = int(input())

only_exts = []
for i in range(N):  # O(N)
    only_exts.append(input().split(".")[1])  # append: O(1)

ext_types = list(set(only_exts))
ext_types.sort()  # O(N*logN)

for ext_type in ext_types:  # O(N)
    print(ext_type, end=" ")
    print(only_exts.count(ext_type))  # O(N) -> 이걸 안쓰고 할 수 있는 방법을 찾아야됨

# 시간복잡도: O(N^2)

"""
