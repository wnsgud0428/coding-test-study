student_list = [i for i in range(1, 31)]
# print(student_list)

for i in range(28):
    student_list.remove(int(input()))

print(min(student_list))
print(max(student_list))
