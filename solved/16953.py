A, B = map(int, input().split())

cnt = 0
while B > A:
    if B % 2 == 0:
        B = B / 2
        # 1번연산
        pass
    elif (B - 1) % 10 == 0:  # 홀수 일때
        B = (B - 1) / 10
        # 2번연산
        pass
    else:
        break
    cnt += 1
    if B == A:
        break

if B == A:
    print(cnt + 1)
else:
    print(-1)
