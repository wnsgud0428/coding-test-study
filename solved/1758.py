N = int(input())
tips = []
for i in range(N):
    tips.append(int(input()))

# print(N, tips)

tips.sort(reverse=True)

sum = 0
for i in range(len(tips)):
    cal = tips[i] - ((i + 1) - 1)
    if cal >= 0:
        sum += cal

print(sum)
