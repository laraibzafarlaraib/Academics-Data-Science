class Department:
    def __init__(self, name, chairman, ID):
        self.name= name
        self.chairman = chairman
        self.ID = ID        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, n):
        self._name = n
    @property
    def chairman(self):
        return self._chairman
    @chairman.setter
    def chairman(self, chman):
        self._chairman = chman
    @property
    def ID(self):
        return self._ID
    @ID.setter
    def ID(self, idd):
        self._ID = idd    
    
    def __str__(self):
        d = ''
        d += 'Department: '
        d += self.name
        d += ', '
        
        d += self.chairman
        return d
class Student:
    def __init__(self, name, rollno, sem, cgpa, depID):
        self.name= name
        self.rollno = rollno
        self.sem = sem
        self.cgpa = cgpa
        self.depID = depID
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, n):
        self._name = n
    @property
    def rollno(self):
        return self._rollno
    @rollno.setter
    def rollno(self, rollno):
        self._rollno = rollno
    @property
    def sem(self):
        return self._sem
    @sem.setter
    def sem(self, sem):
        self._sem = sem
    @property
    def cgpa(self):
        return self._cgpa
    @cgpa.setter
    def cgpa(self, cgpa):
        self._cgpa = cgpa
    @property
    def depID(self):
        return self._depID
    @depID.setter
    def depID(self, depID):
        self._depID= depID   

    def __str__(self):
        j=0
        while j<=5:
            s = self.rollno
            s += self.name
            s += self.sem
            s += self.cgpa
            return s
def main():
    departments= [
        Department("CS Computer Science", "Dr. Jodat Kamal" ,"1"),
        Department("DS Data Science", "Dr. John Doe", "2"),
        Department("IT Information Technology", "Dr. Abbas Ali", "3"),
        Department("SE Software Engineering", "Dr. Sarah Smith", "4")
        ]
    
    students = [
        Student("Laraib Zafar\t\t", "bsdsf22m012\t", "2\t\t", "3.0", "BSDSF22M"),
        Student("Laiba Zafar\t\t", "bsdsf22m013\t", "2\t\t", "1.2", "BSDSF22M"),
        Student("Tooba Zafar\t\t", "bsdsf22m014\t", "2\t\t", "2.7", "BSDSF22M"),
        Student("Talha Zafar\t\t", "bsdsf22m015\t", "2\t\t", "1.6", "BSDSF22M"),
        ]
    

    # Print department-wise student list
    for department in departments:
        print()
        print(department)
        s = 'Roll no\t\tName\t\t\tSemester\tCGPA'
        print(s)
        for student in students:
            print(student)

    # Print students with CGPA less than 1.70
    print()
    print("Students with CGPA less than 1.70")
    for student in students:
        if student.cgpa < "1.70":
            print(student)

if __name__=="__main__":
    main()
