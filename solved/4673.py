N = int(input())
words = []
for _ in range(N):
    words.append(input())
# print(N, words)
group_words = []


for word in words:
    check = []
    is_group_word = True
    for letter in word:
        if letter in check:
            if check[-1] != letter:
                # print(letter)
                is_group_word = False
                break
        else:
            check.append(letter)
    if is_group_word:
        group_words.append(word)

print(len(group_words))
