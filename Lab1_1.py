class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = list(map(float, grades.split(',')))

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        if self.average_grade() >= 4.5:
            return True
        else:
            return False

def main():
    with open('students.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    students = []
    for line in lines:
        data = line.strip().split(';')
        if len(data) != 3:
            continue

    name, group, grades = data
    student = Student(name, group, grades)
    students.append(student)

    groups_avg = {}

    with open('excellent_students.txt', 'w') as output_file:
        for student in students:
            avg_grade = student.average_grade()
            print(f"{student.name}: {avg_grade:.2f}")

            if student.is_excellent():
                output_file.write(f"{student.name} - {student.group}\n")

            if student.group not in groups_avg:
                groups_avg[student.group] = {'sum': 0, 'count': 0}
            groups_avg[student.group]['sum'] += avg_grade
            groups_avg[student.group]['count'] += 1

    print("\nСредний балл по группам:")
    for group, info in groups_avg.items():
        avg_group_grade = info['sum'] / info['count']
        print(f"Группа {group}: {avg_group_grade:.2f}")


if __name__ == "__main__":
    main()