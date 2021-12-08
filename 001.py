    
    
    
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['courses'])
print(student.get('phone', 'Not Found'))

student['phone'] = 4555555


age = student.pop('age')
student.update({'name': 'Jane', 'age': 30})
del student ['age']
print(student)

print(len(student))

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)



