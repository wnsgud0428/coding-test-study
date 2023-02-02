A, B = map(int, input().split())
A_str = str(A)
B_str = str(B)

new_A_str = A_str[2] + A_str[1] + A_str[0]
new_B_str = B_str[2] + B_str[1] + B_str[0]

s_A = int(new_A_str)
s_B = int(new_B_str)

if s_A > s_B:
    print(s_A)
else:
    print(s_B)
