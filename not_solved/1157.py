s = input()

dic = {}
for c in s:
    c = c.upper()
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

# print(dic)
# print(dic.values())

max_value = max(dic.values())
if list(dic.values()).count(max_value) >= 2:
    print("?")
else:
    for key, value in dic.items():
        if value == max_value:
            print(key)
