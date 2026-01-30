class Person:
    def __init__(self, pid , name , age):
        self.gid = pid
        self.name = name
        self.age =age

    def __str__(self):
        return f"{self.pid} , {self.name} , {self.age}"