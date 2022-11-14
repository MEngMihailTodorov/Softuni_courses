n = int(input())
student_dict = {}

for i in range(n):
    name, grade = input().split()

    if name not in student_dict.keys():
        d = {name: [float(grade)]}
        student_dict.update(d)
    else:
        student_dict[name].append(float(grade))


for students, grades in student_dict.items():
    grades_list = " ".join(str(f"{grade:.2f}") for grade in grades)
    average = sum(grades) / len(grades)
    print(f"{students} -> {grades_list} (avg: {average:.2f})")


