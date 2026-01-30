class Dog:
    def __init__(self,name,age):
        self.name = "Buddy"
        self.age = age

    def info(self):
        print(f"{self.name} is {self.age} year old")

def main():
    my_dog = Dog("Buddy ",3)
    my_dog.info()
    your_dog = Dog("Paulie",3)
    your_dog.info()
                   


if __name__ == "__main__":
    main()
