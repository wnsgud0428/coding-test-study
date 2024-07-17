A, B, C = int(input()), int(input()), int(input())
s = str(A * B * C)

dic = {}
for c in s:
    c = int(c)
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

for i in range(10):
    if i in dic:
        print(dic[i])
    else:
        print(0)
