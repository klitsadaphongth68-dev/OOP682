from models.staff import Staff
from models.person import Person
from models.student import Student

student = Student(123456789,"M",20,"s1234")
staff = Staff(123456789,"L",22,"L1234")
print(f"student: {student.name},Age{student.age},Student_ID{student.student.id}")
print(f"staff: {staff.name} ,Age{staff.age},Staff_id{staff.staff.id}")

def get_person_info(person):
    print(isinstance(person, Person))
    return f"name: {person.name} , Age{person.age}"
get_person_info(student)
get_person_info(staff)