switch_num = int(input())
switch_state = list(map(int, input().split()))
switch_state.insert(0,None)

# print("switch", switch_num, switch_state)

student_num = int(input())
student_info = []
for i in range(student_num):
    student_info.append(tuple(map(int, input().split())))

# print("studnet", student_num, student_info)

for info in student_info:
    if info[0] == 1: #남자
        mult = info[1]
        i = 1
        while True:
            if mult*i > switch_num:
                break
            switch_state[mult * i] = int(not switch_state[mult * i])
            i+= 1
    elif info[0] == 2: #여자
        switch_state[info[1]] = int(not switch_state[info[1]])
        l,r = info[1],info[1]
        while True:
            l -= 1
            r += 1
            if l <= 0 or r > switch_num:
                break
            if switch_state[l] != switch_state[r]:
                break
            switch_state[l] = int(not switch_state[l])
            switch_state[r] = int(not switch_state[r])
# print(switch_state)

for i in range(1, switch_num+1):
    print(switch_state[i],end=" ")
    if i % 20 == 0:
        print()