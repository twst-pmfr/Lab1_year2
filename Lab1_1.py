class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def average_grade(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def is_excellent(self):
        if self.average_grade() >= 4.5:
            return True
        else:
            return False

#Основная программа

#1. Читаем студентов из текстового файла
def students_from_file():
    with open('students.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    students_list = []
    for line in lines:
        parts = line.strip().split(';')
        if len(parts) != 3:
            print(f"Ошибка чтения строки: {line}")
            continue

        name = parts[0]
        group = parts[1]
        grades = list(map(float, parts[2].split(',')))

        student = Student(name, group, grades)
        students_list.append(student)

    for s in students_list:
        avg_grade = s.average_grade()
        excellent_status = s.is_excellent()
        print(f"Имя: {s.name}, Группа: {s.group}, Средний бал: {avg_grade:.2f}, Отличник: {excellent_status}")
    return students_list

#2. Записываем отличников в файл excellent_students.txt
def excellent_students_list(students):
    with open('excellent_students.txt', 'w', encoding='utf-8') as file:
        for student in students:
            if student.is_excellent():
                file.write(f"{student.name} - {student.group}\n")

#3. Посчитаем средний бал групп
'''def calculate_group_averages(students):
    group_data = {}
    for student in students:
        group = student.group
        grade_avg = student.average_grade()
        if group not in group_data:
            group_data[group] = {"total": 0, "count": 0}
            group_data["total"] += grade_avg
            group_data["count"] += 1

    result = {}
    for group, data in group_data.items():
        result[group] = round(data["total"] / data["count"], 2)
    return result'''

def main():
    students = students_from_file()
    excellent_students_list(students)
    '''group_averages = calculate_group_averages(students)
    for group, avg in group_averages.items():
        print(f"Группа {group}: Среднее значение - {avg}")'''

if __name__ == "__main__":
    main()