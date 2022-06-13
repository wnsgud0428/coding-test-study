N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
# print(N, K, coins)

num = 0

for c in coins:
    share = K // c
    K -= share * c
    num += share
    if K == 0:
        break

print(num)
