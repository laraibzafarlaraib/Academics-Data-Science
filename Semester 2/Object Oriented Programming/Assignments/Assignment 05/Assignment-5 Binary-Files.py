import struct

class Student:
    def add_student(self):
        n = int(input("How many students data you want to enter? "))
        with open('BinaryStudentData.bin', 'ab') as file:
            student_format = '11s 30s 2s I f 11s'
            
            for _ in range(n):
                roll_no = input('Enter roll number of student:')
                name = input('Enter name of student:')
                dep_code = input('Enter Department code of student:')
                semester = input('Enter semester of student:')
                marks = input('Enter last semester percent marks of student:')
                phoneNo = input('Enter Phone Number of student:')
        
            if Student.student_exists(roll_no):  #(check for NO duplicates)
                print(f'Student with roll number {roll_no} already exists.')

            else: 
                student_data = struct.pack(student_format, roll_no.encode(), name.encode(), dep_code.encode(), int(semester), float(marks), phoneNo.encode())
                file.write(student_data + b'\n')            
                print(f'Student with roll number {roll_no} added succssfully into data base.')

    @staticmethod
    def student_exists(roll_no):
        with open('BinaryStudentData.bin', 'rb') as file:
            student_format = '11s 30s 2s I f 11s'
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            for record in split_records:
                existing_rollno = struct.unpack('11s', record[:11])[0].decode().strip()
                if existing_rollno == roll_no:
                    return True
        return False
    
    def view_student(self, roll_no):
        with open('BinaryStudentData.bin', 'rb') as file:
            student_format = '11s 30s 2s I f 11s'
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            for record in split_records:
                existing_rollno = struct.unpack('11s', record[:11])[0].decode().strip()
                if existing_rollno == roll_no:
                    roll_no, name, dep_code, semester, marks, phoneNo = struct.unpack(student_format, record)
                    print(f'Roll number: {roll_no.decode().strip()}')
                    print(f'Name: {name.decode().strip()}')
                    print(f'Department Code: {dep_code.decode().strip()}')
                    print(f'Semester: {semester}')
                    print(f'Marks of Last Semester: {marks}')
                    print(f'Phone number: {phoneNo.decode().strip()}')
                    print()
                    break  
            else:
                print('Student with the given roll number not found.')
   
    def edit_student(self, roll_no):
        print('Enter the details of this student again to edit it in records.')
        with open('BinaryStudentData.bin', 'ab') as file:
            student_format = '11s 30s 2s I f 11s'

            roll_no = input('Enter roll number of student:')
            name = input('Enter name of student:')
            dep_code = input('Enter Department code of student:')
            semester = input('Enter semester of student:')
            marks = input('Enter last semester percent marks of student:')
            phoneNo = input('Enter Phone Number of student:')

            student_data = struct.pack(student_format, roll_no.encode(), name.encode(), dep_code.encode(), int(semester), float(marks), phoneNo.encode())
            file.write(student_data + b'\n')            
            print(f'Student with roll number {roll_no} edited succssfully into data base.')

    def delete_student(self, roll_no):
            with open('BinaryStudentData.bin', 'r+b') as file:
                student_format = '11s 30s 2s I f 11s'
                binary_data = file.read()
                split_records = binary_data.split(b'\n')[:-1]

                found = False
                updated_data = b''

                for record in split_records:
                    existing_rollno = struct.unpack('11s', record[:11])[0].decode().strip()

                    if existing_rollno == roll_no:
                        found = True
                    else:
                        updated_data += record + b'\n'

                if found:
                    file.seek(0)
                    file.write(updated_data)
                    print(f'Student with roll number {roll_no} deleted successfully.')
                else:
                    print(f'Student with roll number {roll_no} not found in the database.')





    def list_by_sem(self, sem):
        self.sem = sem
        with open('BinaryStudentData.bin', 'rb') as file:
            student_format = '11s 30s 2s I f 11s'
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            for record in split_records:
                roll_no, name, dep_code, semester, marks, phoneNo = struct.unpack(student_format, record)
                #print({semester})
                #print(self.sem)
                if int(semester) == int(self.sem):
                    print(f'Semester: {semester}')
                    print(f'Roll number: {roll_no.decode().strip()}')
                    print(f'Name: {name.decode().strip()}')
                    print(f'Department Code: {dep_code.decode().strip()}')
                    print(f'Marks of Last Semester: {marks}')
                    print(f'Phone number: {phoneNo.decode().strip()}')
                    print()
                

    def list_by_name(self, n):
        self.n = n
        with open('BinaryStudentData.bin', 'rb') as file:
            student_format = '11s 30s 2s I f 11s'
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            for record in split_records:
                roll_no, name, dep_code, semester, marks, phoneNo = struct.unpack(student_format, record)
                if str(name.decode().strip().lower()) == str(self.n.strip().lower()):
                    print(f'Name: {name.decode().strip()}')
                    print(f'Semester: {semester}')
                    print(f'Roll number: {roll_no.decode().strip()}')
                    print(f'Department Code: {dep_code.decode().strip()}')
                    print(f'Marks of Last Semester: {marks}')
                    print(f'Phone number: {phoneNo.decode().strip()}')
                    print()
               

    def print_std_list(self):
        with open('BinaryStudentData.bin', 'rb') as file:
            student_format = '11s 30s 2s I f 11s'
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            for record in split_records:
                roll_no, name, dep_code, semester, marks, phoneNo = struct.unpack(student_format, record)
                print()
                print(f'Roll number: {roll_no.decode().strip()}')
                print(f'Name: {name.decode().strip()}')
                print(f'Department Code: {dep_code.decode().strip()}')
                print(f'Semester: {semester}')
                print(f'Marks of Last Semester: {marks}')
                print(f'Phone number: {phoneNo.decode().strip()}')
                
    def transcript(self, start_roll_no, end_roll_no):
        with open('BinaryStudentData.bin', 'rb') as file:
            student_format = '11s 30s 2s I f 11s'
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            for record in split_records:
                roll_no, name, dep_code, semester, marks, phoneNo = struct.unpack(student_format, record)
                existing_rollno = roll_no.decode().strip()

                if start_roll_no <= existing_rollno <= end_roll_no:
                    print(f'Roll number: {existing_rollno}')
                    print(f'Name: {name.decode().strip()}')
                    print(f'Department Code: {dep_code.decode().strip()}')
                    print(f'Semester: {semester}')
                    print(f'Marks of Last Semester: {marks}')
                    print(f'Phone number: {phoneNo.decode().strip()}')
                    print()

class Grades(Student):
    def add_grades(self):
        with open('BinaryStudentGradeData.bin', 'ab') as file:
            grades_format = '20s 11s 4s'
            
            roll_no = input("Enter the roll number of which you want to add grade: ")
            if Student().student_exists(roll_no):
                course = input('Enter Course Name of this student:')
                try:
                    perc_marks = float(input('Enter Percentage Marks of student: '))
                except ValueError:
                    print("Invalid input for percentage marks. Please enter a numeric value.")
                    return

                grade = Grades.grade(perc_marks)
                packed_data = struct.pack(grades_format, course.encode(),roll_no.encode(), grade.encode())
                
                if Grades.course_grade_exists(roll_no, course):
                    print(f'Student with roll no {roll_no} has alreadyy grade of course {course} in data. try entering new course data.')
                else:
                    file.write(packed_data + b'\n')
                    print(f'Grade added successfully into data!')
            
            else:
                print(f'Student with roll number {roll_no} does not exist in database. Add student first then add grade for them.')
    
    @staticmethod
    def grade(percentage):
        grade = ''
        if percentage >= 85:
            grade = 'A'
        elif 80 <= percentage <= 84:
            grade = 'A-'
        elif 75 <= percentage <= 79:
            grade = 'B+'
        elif 70 <= percentage <= 74:
            grade = 'B'
        elif 65 <= percentage <= 69:
            grade = 'B-'
        elif 61 <= percentage <= 64:
            grade = 'C+'
        elif 58 <= percentage <= 60:
            grade = 'C'
        elif 55 <= percentage <= 57:
            grade = 'C-'
        elif 50 <= percentage <= 54:
            grade = 'D'
        else:
            grade = 'F'
        return grade

    @staticmethod
    def course_grade_exists(roll_no, course):
        with open('BinaryStudentGradeData.bin', 'rb') as file:
            grades_format = '20s 11s 4s'
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            for record in split_records:
                existing_course, existing_rollno, _ = struct.unpack(grades_format, record)
                existing_rollno = existing_rollno.decode().strip()
                existing_course = existing_course.decode().strip()

                
                print(existing_course, existing_rollno)
                print(course , roll_no)
                if str(existing_rollno) == str(roll_no) and str(existing_course) == str(course):
                    return True

        return False


    def import_grades(self):
        with open('BinaryStudentGradeData.bin', 'rb') as file:
            grades_format = '20s 11s 4s'

            course = input('Enter the course name of which grades you want to see:')
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            for record in split_records:
                existing_course, rollno, grade = struct.unpack(grades_format, record)
                #print(existing_course, rollno, grade)

                existing_course = existing_course.decode().strip()
                rollno = rollno.decode().strip()
                grade = grade.decode().strip()

                #print(existing_course, rollno, grade)
                #print(course)
                if str(existing_course) == str(course):
                    print(f'course:{existing_course}')                    
                    print(f'Grade of roll number{rollno}: {grade}')

    def view_grades(self, roll_no):
        self.roll_no = roll_no
        with open('BinaryStudentGradeData.bin', 'rb') as file:
            grades_format = '20s 11s 4s'
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            print(f'Roll Number: {self.roll_no}')
            
            for record in split_records:
                course, existing_rollno, grade = struct.unpack(grades_format, record)
                existing_rollno = existing_rollno.decode().strip()
                course = course.decode().strip()
                grade = grade.decode().strip()

                if existing_rollno == self.roll_no:
                    print(f'Course: {course}')
                    print(f'Grade: {grade}')              

    def edit_grades(self, roll_no):
        pass

    def delete_grade(self, roll_no):
        pass

    def award_sheet(self):
        with open('BinaryStudentGradeData.bin', 'rb') as file:
            grades_format = '20s 11s 4s'
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            pf = []
            oop = []
            dld = []
            maths = []

            for record in split_records:
                course, rollno, _ = struct.unpack(grades_format, record)
                rollno = rollno.decode().strip()
                course = course.decode().strip()

                if course == 'pf':
                    pf.append(rollno)
                elif course == 'dld':
                    dld.append(rollno)
                elif course == 'oop':
                    oop.append(rollno)
                elif course == 'maths':
                    maths.append(rollno)

            self.course_students('Programming Fundamentals', pf)
            self.course_students('Object Oriented Programming', oop)
            self.course_students('Digital Logic Design', dld)
            self.course_students('Mathematics', maths)

    @staticmethod
    def course_students(self, course_name, students):
        print(f'{course_name} has the following students enlisted:')
        if len(students) != 0:
            for i, student in enumerate(students):
                print(f'Student {i + 1}: {student}')
        else:
            print('There are currently no students enrolled in this course.')

    
    def summary_sheet(self):
        with open('BinaryStudentGradeData.bin', 'rb') as file:
            grades_format = '20s 11s 4s'
            binary_data = file.read()
            split_records = binary_data.split(b'\n')[:-1]

            courses = {'pf': [], 'dld': [], 'oop': [], 'maths': []}

            for record in split_records:
                course, rollno, _ = struct.unpack(grades_format, record)
                rollno = rollno.decode().strip()
                course = course.decode().strip()

                if course in courses:
                    courses[course].append(rollno)

            Grades.print_summary(courses)

    @staticmethod
    def print_summary(courses):
        for course_name, students in courses.items():
            print(f'Course: {course_name}')
            if len(students) != 0:
                for student in students:
                    print(f'Student: {student}')
            else:
                print('No students enrolled in this course.')
            print()

def main():
    
    prompt = input('WELCOME to our DBMS! \nTo go into our Databse Management sytem press "D" \nTo Exit our Data managemnet system press "Q":  ')
    
    while prompt!='Q':
        choice = input('Select from below: \n a)Students Data \n b)Grades Data\t')
        
        if choice == 'a':       #reach student data
            menu = input('What do you want to do? \n1)Add a student \n2)View student by roll no \n3)Edit student by roll no \n4)Delete student by roll no \n5)List student by semester \n6)List students by name \n7)Print Students List \n8)Transcripts for a range of students \nSelect From above mentiones choices:')
            
            if menu == '1':    #add
                Student().add_student()

            elif menu == '2':  #view
                roll_no = input('Enter the roll number of student:')
                Student().view_student(roll_no)

            elif menu == '3':  #Edit student
                roll_no = input('Enter the roll number of student whose record you want to edit:')
                Student().edit_student(roll_no)

            elif menu == '4':  #Delete student
                roll_no = input('Enter the roll number of student whose record you want to Delete:')
                Student().delete_student(roll_no)

            elif menu == '5':    #List student by semester 
                sem = input('Enter the semester by ywhich you want to display students: ')
                Student().list_by_sem(sem)

            elif menu == '6':   #List students by name
                n = input('Enter the name of student by you want to see the data:')
                Student().list_by_name(n)

            elif menu == '7':   #Printt students list
                Student().print_std_list()

            elif menu == '8':   #Transcripts for a range of students
                start_roll_no = input('Enter the start roll number:')
                end_roll_no = input('Enter the end roll number:')
                Student().transcript(start_roll_no, end_roll_no)

        elif choice == 'b':    #reach grades data...
            menu2 = input('What do you want to do? \n1)Add grade of a student for a course \n2)Import grades for a course for many students \n3)View grades of a student \n4)List Student wise (1 student) grade of courses \n5)List Course wise grade (1 course) of students \n6)Award sheet (courses one by one, with students enrolled in it) \n7)Summary sheet (courses info, one by one, with one line for each student in it) \nSelect from above mentioned choices:)')

            if menu2 == '1':
                Grades().add_grades()

            elif menu2 == '2':
                Grades().import_grades()

            elif menu2 == '3':
                roll_no = input ('Enter the roll no you want to view:')
                Grades().view_grades(roll_no)

            elif menu2 == '4':
                roll_no = input('Entetr the roll no whose record you want to edit: ')
                Grades().edit_grades(roll_no)

            elif menu2 == '5':
                roll_no = input('Entetr the roll no whose record you want to delete: ')
                Grades().delete_grade(roll_no)

            elif menu2 == '6':
                Grades().award_sheet()
                
            elif menu2 == '7':
                Grades().summary_sheet()

        else:
            choice = input('You entered wrong choice. Please select from below: \na)Students Data \nb)Grades Data\t')
    
main()