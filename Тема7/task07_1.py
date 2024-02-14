class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Saved name "{self.name}" and age "{self.age}"'

stud1 = Student("Pavel", 19)
print(str(stud1))