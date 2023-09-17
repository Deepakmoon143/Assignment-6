class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, skill):
        super().__init__(name, age, coat_color)
        self.skill = skill

    def special_skill(self):
        print(f"{self.name} has a special skill: {self.skill}")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def show_strength(self):
        print(f"{self.name} is known for its strength: {self.strength}")


name = input("Enter the name of the dog: ")
age = input("Enter the age of the dog: ")
coat_color = input("Enter the coat color of the dog: ")


dog = Dog(name, age, coat_color)


print("\nDog Class:")
dog.description()
dog.get_info()


skill = input("Enter a special skill for the Jack Russell Terrier: ")
jack_russell = JackRussellTerrier(name, age, coat_color, skill)


print("\nJackRussellTerrier Class:")
jack_russell.description()
jack_russell.get_info()
jack_russell.special_skill()


strength = input("Enter a strength for the Bulldog: ")
bulldog = Bulldog(name, age, coat_color, strength)


print("\nBulldog Class:")
bulldog.description()
bulldog.get_info()
bulldog.show_strength()
