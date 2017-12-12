class PallidaClass (object):
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.mentors = []
    
    def add_student(self, Student):
        self.students.append(Student)

    def add_mentor(self, Mentor):
        self.mentors.append(Mentor)

    def info(self):
        print("Pallida " + str(self.class_name) + " class has " + str(len(self.students)) + " students and " + str(len(self.mentors)) + " mentors.")