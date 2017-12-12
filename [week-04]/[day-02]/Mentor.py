from People import Person

class Mentor(Person):
    def __init__(self, name, age, gender, level):
        super().__init__(name, age, gender)
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level

    def get_goal(self):
        print("My goal is: Educate brilliant junior software developers.")

    def introduce(self):
        print("Hi, I'm " + str(self.name) + " a " + str(self.age) + " year old " + str(self.gender) + " " + str(self.level) + " mentor.")