from People import Person

class Student(Person):
    def __init__(self, name, age, gender, previous_organization):
        super().__init__(name, age, gender)
        self.name = name
        self.age = age
        self.gender = gender
        self.previous_organization = previous_organization
        self.skipped_days = 0

    def get_goal(self):
        print("My goal is: Be a junior software developer.")

    def introduce(self):
        print("Hi, I'm " + str(self.name) + " a " + str(self.age) + " year old " + str(self.gender) + " from " + str(self.previous_organization) + " who skipped " + str(self.skipped_days) + " days from the course already.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days