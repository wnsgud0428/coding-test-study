S = input()
S = list(S)
isInTag = False
for i in range(len(S)):
    if S[i] == "<":
        isInTag = True
    if S[i] == ">":
        isInTag = False
    if isInTag == True and S[i] == " ":
        S[i] = "@"
S = "".join(S)
# print(S)

S = S.replace("<", " <")
S = S.replace(">", "> ")
# print(S)

S = S.split(" ")
# print(S)

new_S = []
for w in S:
    if w == "":
        continue
    if w.startswith("<") == False:
        w = w[::-1]
        w = "W" + w + "W"
    new_S.append(w)

new_S = "".join(new_S)
new_S = new_S.replace("WW", " ").replace("W", "").replace("@", " ")
print(new_S)
