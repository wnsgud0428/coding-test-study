money = int(input())
stocks = list(map(int, input().split()))
# print(money, stocks)

# BNP
BNP_money = money
BNP_stock_count = 0

for s in stocks:
    while BNP_money >= s:
        BNP_money -= s
        BNP_stock_count += 1

BNP_sum = BNP_money + (BNP_stock_count * stocks[13])
# print(BNP_sum)


# TIMING
t_money = money
t_stock_count = 0

prev_price = s[0]
up_count = 0
down_count = 0
for s in stocks:
    if stocks.index(s) > 0:
        if s > prev_price:  # 가격이 오른 경우
            up_count += 1
            down_count = 0
        elif s < prev_price:  # 내린 경우
            down_count += 1
            up_count = 0
    if up_count >= 3:  # 전량 매도
        t_money += t_stock_count * s
        t_stock_count = 0
    elif down_count >= 3:  # 전량 매수
        while t_money >= s:
            t_money -= s
            t_stock_count += 1
    prev_price = s

t_sum = t_money + (t_stock_count * stocks[13])
# print(t_sum)


if BNP_sum > t_sum:
    print("BNP")
elif BNP_sum < t_sum:
    print("TIMING")
else:
    print("SAMESAME")
