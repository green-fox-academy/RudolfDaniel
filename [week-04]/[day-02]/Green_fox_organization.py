from People import Person
from Student import Student
from Mentor import Mentor
from Sponsor import Sponsor
from PallidaClass import PallidaClass

people = []

mark = Person("Mark", 46, "male")
people.append(mark)
jane = Person("Jane Doe", 30, "female")
people.append(jane)
john = Student("John Doe", 20, "male", "BME")
people.append(john)
jane2 = Student("Jane Doe", 30, "female", "The School of Life")
people.append(jane2)
gandhi = Mentor("Gandhi", 148, "male", "senior")
people.append(gandhi)
jane3 = Mentor("Jane", 30, "female", "intermediate")
people.append(jane3)
jane4 = Sponsor("Jane", 30, "female", "Google")
people.append(jane4)
elon = Sponsor("Elon Musk", 46, "male", "SpaceX")
people.append(elon)

for i in range(3):
    jane2.skip_days(1)

for i in range(3):
    elon.hire()

for i in range(5):
    jane4.hire()

for member in people:
    member.introduce()
    member.get_goal()

lagopus = PallidaClass('BADA55')
lagopus.add_student("Jane Doe")
lagopus.add_student(john)
lagopus.add_mentor("Yoda")
lagopus.add_mentor(gandhi)
lagopus.info()