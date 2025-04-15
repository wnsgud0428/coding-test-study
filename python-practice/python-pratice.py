# for i in range(5):
#     print(i)

# names = ["mike", "jane", "tom"]
# print(names)

# user = {}
# user["age"] = 25
# print(user)

# arr = [[2, 4], [5, 3], [2, 3], [1, 99]]
# arr.sort(key=lambda x: (x[0], -x[1]))
# print(arr)

""" -------------------------------------------------------------"""

# arr = []
# for i in range(5):
#     arr.append(i)

# dic = dict()

# dic["a"] = 3
# dic["b"] = 4
# print(dic)

# print(list(dic.values()))

# tup = tuple([1, 2, 3])
# print(tup)

""" -------------------------------------------------------------"""
fruit = [
    "사과",
    "사과",
    "바나나",
    "바나나",
    "딸기",
    "키위",
    "복숭아",
    "복숭아",
    "복숭아",
]  # 배열을 만들어 변수 fruit 에 담음

d = {}  # 빈 딕셔너리 만들어 , 변수 d 에 저장

for f in fruit:  # 배열내 데이터 존재 여부 체크, 후 f 에 담는다.
    if f in d:  # f에 사과라는 key 가 , d 딕셔너리에 있어?
        d[f] += 1
        # 그렇다면, f(key 값 사과) 의 value 갯수를 하나 올려줘
    else:
        d[f] = 1
        # 만약 d 딕셔너리에 사과라는 key 가 없다면, 그걸 d 딕셔너리  에 넣고 밸류는 1로 만들어줘


print(d)  # d 딕셔너리 내용을 출력해
