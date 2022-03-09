# 8진수 2진수

dec_conv = {
    "0": "000",
    "1": "001",
    "2": "010",
    "3": "011",
    "4": "100",
    "5": "101",
    "6": "110",
    "7": "111",
}

num = input()
binary_num = ""

for n in num:
    binary_num += dec_conv[n]

index = 0
for i in range(len(binary_num)):
    if binary_num[i] == "1":
        index = i
        break

print(binary_num[i:])
