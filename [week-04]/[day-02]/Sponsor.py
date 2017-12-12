from People import Person

class Sponsor(Person):
    def __init__(self, name, age, gender, company):
        super().__init__(name, age, gender)
        self.name = name
        self.age = age
        self.gender = gender
        self.company = company
        self.hired_students = 0

    def get_goal(self):
        print("My goal is: Hire brilliant junior software developers.")

    def introduce(self):
        print("Hi, I'm " + str(self.name) + " a " + str(self.age) + " year old " + str(self.gender) + " who represents " + str(self.company) + " and hired " + str(self.hired_students) + " students so far.")

    def hire(self):
        self.hired_students += 1