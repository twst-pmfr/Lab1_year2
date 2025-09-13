import statistics
student = {'name': 'Alice', 'age': 20, 'course': 'Math' , 'grades': [5, 4, 5]}
print(student['name'],student['course'])
print(statistics.mean(student['grades']))
student['grades'].append(5)
print(student)