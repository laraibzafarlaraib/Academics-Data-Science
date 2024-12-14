import struct

# Writing binary data to the file
n = int(input("How many students data you want to enter? "))

with open('BinaryWriting.bin', 'ab') as file:
    student_format = '11s 30s 2s I f 11s'

    for _ in range(n):
        roll_no = input('Enter roll number of student:')
        name = input('Enter name of student:')
        dep_code = input('Enter Department code of student:')
        semester = input('Enter semester of student:')
        marks = input('Enter last semester percent marks of student:')
        phoneNo = input('Enter Phone Number of student:')

        student_data = struct.pack(student_format, roll_no.encode(), name.encode(), dep_code.encode(), int(semester), float(marks), phoneNo.encode())
        file.write(student_data + b'\n')

# Reading binary data from the file
with open('BinaryWriting.bin', 'rb') as binaryfile:
    binary_data = binaryfile.read()
    records = binary_data.split(b'\n')[:-1]
    # Split by newline and remove the last empty record

    for record in records:
        roll_no, name, dep_code, semester, marks, phoneNo = struct.unpack(student_format, record)
        print(f'Roll number: {roll_no.decode().strip()}')
        print(f'Name: {name.decode().strip()}')
        print(f'Department Code: {dep_code.decode().strip()}')
        print(f'Semester: {semester}')
        print(f'Marks of Last Semester: {marks}')
        print(f'Phone number: {phoneNo.decode().strip()}')
        print()
