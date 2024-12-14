
def subjects(file, parts):
    with open('newgrades.txt', 'r') as f:
        f.seek(2)
        itc = dld = pf = 0
        i=0
        course = []
        while i<3:
            subject = int(parts[5]+parts[6]+parts[4])
            course.append(subject)
            f.readline()
            i += 1
        itc += course[0]
        pf += course[1]
        dld += course[2]
    return itc, pf, dld

def total(file, parts):
    with open('newgrades.txt', 'r') as f:
        f.seek(2)
        total = 0
        for i in range(3):
            subject = int( parts[5] + parts[6] +parts[4])
            total += subject
            f.readline()
    return total

def percentage(total):
    age = (total/300)*100
    return age

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

def degree_avg():
    itc = dld = pf = 0
    for j in range(3):
        i=0
        course = []
        while i<3:
            subject = sum(parts[5],parts[6],parts[4])
            course.append(subject)
            gfile.readline()
            i += 1
        itc += course[0]
        pf += course[1]
        dld += course[2]
    avg1 = int(itc)/3
    avg2 = int(pf)/3
    avg3 = int(dld)/3
    average = (avg1+avg2+avg3)/3
    return avg1, avg2, avg3, average
    
def main():
    report_file = 'report.txt'
    grades_file = 'newgrades.txt'

    with open(report_file, 'w') as ifile, open(grades_file, 'r') as gfile:
        ifile.write(f'\t\tUniversity of the Punjab\n\t\tCollege of Information Technology\n\t\tResult of session: spring 2023')
        
        ifile.write(f'\nDegree: BIT\n')
        ifile.write(f'\nSr.No. Roll No.   Student Name          ITC  PF  DLD  TOTAL  %age  Grade')
        ifile.write(f'\n====== ========== ===================== ===  ==  ===  =====  ====  =====')
        #skipping header lines
        next(gfile)
        next(gfile)
        #lists for storing students
        bit_students = []
        bsef_students = []
        
        for student in gfile:
            file_path = grades_file
            parts = student.split()
            if parts[0].startswith("BITF"):

                ITC , PF , DLD = subjects(gfile, parts)
                total_marks = total(gfile, parts)
                percentage_value = percentage(total_marks)
                grade_value = grade(percentage_value)

                bit_students.append(parts[0])        
                bit_students.append(parts[1])
                bit_students.append(parts[2])
                bit_students.append(ITC)
                bit_students.append(PF)
                bit_students.append(DLD)
                bit_students.append(total_marks)
                bit_students.append(percentage_value)
                bit_students.append(grade_value)
                
            elif parts[0].startswith("BSEF"):
                ITC , PF , DLD = subjects(gfile, parts)
                total_marks = total(gfile, parts)
                percentage_value = percentage(total_marks)
                grade_value = grade(percentage_value)

                bsef_students.append(parts[0])        
                bsef_students.append(parts[1])
                bsef_students.append(parts[2])
                bsef_students.append(ITC)
                bsef_students.append(PF)
                bsef_students.append(DLD)
                bsef_students.append(total_marks)
                bsef_students.append(percentage_value)
                bsef_students.append(grade_value)
                print(bsef_students)
                # Skipping two lines
                next(gfile)
                next(gfile)

        # Writing BIT students
        for i in range(0, len(bit_students), 3):
            ifile.write(f'\n{i//3 + 1}      {bit_students[0]} {bit_students[1]} {bit_students[2]}           {bit_students[3]} {bit_students[4]} {bit_students[5]} {bit_students[6]} {bit_students[7]}')
            print()
        ifile.write(f'\n\nDegree: BSEF\n')
        ifile.write(f'\nSr.No. Roll No.   Student Name          ITC  PF  DLD  TOTAL  %age  Grade')
        ifile.write(f'\n====== ========== ===================== ===  ==  ===  =====  ====  =====')

        # Writing BSEF students
        for i in range(0, len(bsef_students), 3):
            print()
           # ifile.write(f'\n{i//3 + 1}      {bsef_students[i]} {bsef_students[i+1]} {bsef_students[i+2]} {bit_students[i+3]} {bit_students[i+4]} {bit_students[i+5]}')


main()
