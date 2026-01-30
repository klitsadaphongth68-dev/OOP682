from models.classroom import Classroom
from models.student import Student

oop = Classroom("OOP")
oop.add_student(Student(1, "Alice",20,"S001"))
oop.add_student(Student(2,"Bob",22,"S002"))
print(f"{oop.name} registered {len(oop)} student")
oop.add_Student(Student(3,"Charlie",21,"S003"))
print(len(oop))
print("Student in the class")
for i in range(len(oop)):
    print(oop[i])