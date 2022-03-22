board = input()
splited = board.split(".")

flag = True
new_board = []
for s in splited:
    if "X" in s:  # X가 한개 이상 있어야 진행, 없으면 위의 for문 돔
        if not (len(s) % 2 == 0):
            flag = False
            break
        else:  # X가 2의 배수개 만큼 있는 경우
            if len(s) % 4 == 0:
                new_s = s.replace("X", "A")
                new_board.append(new_s)
                # print(new_s)
            else:  # len(s) % 2 == 0인 경우
                # 끝을 BB로 변경후, 나머지 X를 A로 바꿈
                new_s = s.removesuffix("XX")
                new_s += "BB"
                new_s = new_s.replace("X", "A")
                new_board.append(new_s)
                # print(new_s)
    else:
        new_board.append(s)

if flag == True:
    print(".".join(new_board))
else:
    print("-1")
