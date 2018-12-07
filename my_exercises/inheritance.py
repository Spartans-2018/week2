class Pet:
    eyes = 2
    legs = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("You got new pet")

    def jump(self):
        print(f"{(self.name)}  jumps")

class Dog(Pet):
    def __init__(self):
        super().__init__("tom", 15)

    def eat(self):
        print(f"{self.name} eats")

    def jump(self, a):
        print(f"jump in Dog {a}")

dog = Dog()
dog.eat()
dog.jump("high")

pet = Pet("saas", 12)
pet.jump()
