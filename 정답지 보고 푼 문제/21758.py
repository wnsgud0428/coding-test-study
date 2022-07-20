N = int(input())
p = list(map(int, input().split()))  # place
ans = 0  # 최대가 되야함

### 구간합 구하기
p_ss = [0 for i in range(N)]  # prefix_sums
for i in range(N):
    if i == 0:
        p_ss[i] = p[0]
    else:
        p_ss[i] = p_ss[i - 1] + p[i]
# print(p_ss)


### 벌꿀벌 케이스
hap = sum(p[1 : N - 2 + 1]) + max(p[1 : N - 2 + 1])
ans = max(hap, ans)

### 벌벌꿀 케이스
for i in range(1, N - 2 + 1):
    # 꿀벌1
    bee1 = p_ss[-1] - p[0] - p[i]
    bee2 = p_ss[-1] - p_ss[i]
    ans = max(bee1 + bee2, ans)

### 꿀벌벌 케이스
# 뒤집기 작업
p_r = list(reversed(p))
p_ss_r = [0 for i in range(N)]  # prefix_sums_reversed
for i in range(N):
    if i == 0:
        p_ss_r[i] = p_r[0]
    else:
        p_ss_r[i] = p_ss_r[i - 1] + p_r[i]


for i in range(1, N - 2 + 1):
    # 꿀벌1
    bee1 = p_ss_r[-1] - p_r[0] - p_r[i]
    bee2 = p_ss_r[-1] - p_ss_r[i]
    ans = max(bee1 + bee2, ans)


print(ans)
