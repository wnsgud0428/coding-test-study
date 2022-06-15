formula = input()
only_number = list(map(int, formula.replace("+", "-").split("-")))

only_sign = []
for f in formula:
    if f == "+" or f == "-":
        only_sign.append(f)

# print(only_number, only_sign)

minus_position = "".join(only_sign).find("-")


total = 0
if minus_position == -1:
    total = sum(only_number)
else:
    for i in range(0, minus_position + 1):
        total += only_number[i]
    for i in range(minus_position + 1, len(only_number)):
        total -= only_number[i]


print(total)
