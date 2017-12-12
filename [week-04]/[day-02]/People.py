class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hi, I'm " + str(self.name) + " a " + str(self.age) + " year old " + str(self.gender) + ".")
    
    def get_goal(self):
        print("My goal is: Live for the moment!")