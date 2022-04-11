N = int(input())
prices = []
for i in range(N):
    prices.append(int(input()))

# print(N, prices)

prices.sort(reverse=True)

sum = 0
for i in range(len(prices)):
    if not (i % 3 == 2):
        sum += prices[i]
print(sum)
