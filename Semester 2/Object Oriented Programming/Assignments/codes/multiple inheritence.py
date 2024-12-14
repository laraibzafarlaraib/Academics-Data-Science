
class Person:
    def __init__(self, name = str, contactNo = int):
        self.name = name
        self.contactNo = contactNo

    
class Student(Person):
    def __init__(self, name = str, contactNo = int, department = str, semster = int):
        super().__init__(name, contactNo)
        self.dep = department
        self.sems = semster

    def __str__(self):
        return f'Name: {self.name} \nContact Number: {self.contactNo} \nDepartment: {self.dep} \nSemster:{self.sems}'

class Teacher(Person):
    def __init__(self, name = str, contactNo = int , course = str, officeNumber= int):
        super().__init__(name, contactNo)
        self.course = course
        self.officeNo = officeNumber
    def __str__(self):
        return f'Name: {self.name} \nContact Number: {self.contactNo} \nCourse: {self.course} \nOffice Number:{self.officeNo}'

class TA(Student, Teacher):
    def __init__(self, name=str, contactNo=int, course=str, officeNumber=int, department=str, semester=int):
        Student.__init__(self, name, contactNo, department, semester)
        Teacher.__init__(self, name, contactNo, course, officeNumber)

    def __str__(self):
        student_info = super(Student, self).__str__()
        teacher_info = Teacher.__str__(self)
        return f'{student_info}\n{teacher_info}'

def main():
    s1 = Student('Laraib', 1122, 'Data science', 2)
    s2 = Student('LAiba', 3344, 'Data science', 2)
    print(f'Students are: \n{s1}\n{s2}')

    t1 = Teacher('Muhammad Idrees', '5566', 'Object Oriented Programming', 101)
    t2 = Teacher('Arif Butt', '7788', 'DLD', 202)
    print(f'\nTeachers are:\n{t1}\n{t2}')

    ta1 = TA('Ali', 9900, 'Data Science', 1, 'Machine Learning', 303)
    print(f'\nTeaching Assistant is:\n{ta1}')


main()