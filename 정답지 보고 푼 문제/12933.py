sounds = input()

visited = [False for i in range(len(sounds))]
q_count = sounds.count("q")


stack = ""
duck_count = 0
is_duck_here = False
for j in range(q_count):
    for i in range(len(sounds)):
        if visited[i] == True:
            continue
        else:
            # 작업 진행
            if stack == "" and sounds[i] == "q":
                stack += sounds[i]
                visited[i] = True
            elif stack == "q" and sounds[i] == "u":
                stack += sounds[i]
                visited[i] = True
            elif stack == "qu" and sounds[i] == "a":
                stack += sounds[i]
                visited[i] = True
            elif stack == "qua" and sounds[i] == "c":
                stack += sounds[i]
                visited[i] = True
            elif stack == "quac" and sounds[i] == "k":
                stack = ""
                visited[i] = True
                is_duck_here = True
    stack = ""
    if is_duck_here == True:
        duck_count += 1
        is_duck_here = False

### 정답지를 본 부분
### 녹음소리가 올바르지 않게 녹음된 경우를 생각하는 것이 어려웠다!
if False in visited or len(sounds) % 5 != 0 or duck_count == 0:
    print("-1")
else:
    print(duck_count)
