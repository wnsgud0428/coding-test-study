# 최소, 최대 2
T = int(input())
arr = [[] for i in range(T)]

for i in range(T):
    N = int(input())
    arr[i] = list(map(int, input().split()))

for inner_arr in arr:
    print(min(inner_arr), max(inner_arr))
