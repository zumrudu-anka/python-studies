class Student():
    def study(self):
        print("This student studying now...")

class Laborer():
    def work(self):
        print("The Laborer is working now...")

class Programmer(Student,Laborer):
    pass

programmer=Programmer()
programmer.study()
programmer.work()