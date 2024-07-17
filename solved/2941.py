X = int(input())
start = 1
increase = 1

step = 1
more = 0

while True:
    if start == X:
        more = 0
        break
        # step 값으로 start_a, start_b 구할 수 있음
    elif start > X:
        step -= 1
        start -= increase - 1
        more = X - start
        # print("here", start, increase)
        break
    step += 1
    start += increase
    increase += 1
    # print("step&start", step, start)

""" 처리 """
numer = None
denom = None
if step % 2 == 1:
    numer = step
    denom = 1
    numer -= more
    denom += more
else:  # 짝수 단계
    numer = 1
    denom = step
    numer += more
    denom -= more

# print(step, more)
print(str(numer) + "/" + str(denom))
