def convert(s):
    num = 1
    if "K" in s:
        num = num * 5

    num = num * 10 ** (len(s) - 1)

    return num


s = input()

origin_s = s

s_for_max = s.replace("K", "K/")
s_for_max_splited = s_for_max.split("/")
if s_for_max_splited[-1] == "":
    s_for_max_splited.pop()  # del 대신 pop쓰면 안되나? 시간 복잡도면에서 유리해보임..
if "K" not in s_for_max_splited[-1]:
    temp = list(s_for_max_splited[-1])
    s_for_max_splited.pop()
    s_for_max_splited.extend(temp)

# print(s_for_max_splited)


s_for_min = s.replace("K", "/K/").replace("//", "/")
s_for_min_splited = s_for_min.split("/")
if s_for_min_splited[-1] == "":
    s_for_min_splited.pop()
if s_for_min_splited[0] == "":
    s_for_min_splited.pop(0)
# print(s_for_min_splited)

MAX = ""
for e in s_for_max_splited:
    MAX += str(convert(e))
print(int(MAX))

MIN = ""
for e in s_for_min_splited:
    MIN += str(convert(e))
print(int(MIN))
