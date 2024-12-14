import json

data = {} # course data

def save_data(courses_data):
    with open('courses_data.json', 'w') as file:
        json.dump(courses_data, file)

def load_data():
    try:
        with open('courses_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def display_menu():
    print('\nMenu:')
    print('a) ADD \ns) Search\nd) Delete\nl) List ALL\ne) Edit\nq) Quit')
    print('Select from above.')

def add():
        
    code = input("Enter course code (max 8 characters): ")
    title = input("Enter course title (max 40 characters): ")
    credits = input("Enter credits hour: ")
    semester = input("Enter default semester: ")
    course_type = input("Enter course type (core or elective): ")

        
    data[code] = {
            'title': title,
            'credits': credits,
            'semester': semester,
            'type': course_type
        }
    print("Course added successfully!")
    

def search():
    code = input("Enter course code to search: ")
    if code in data:
        print("Course found:")
        print(data[code])
    else:
        print("Course not found.")

def delete():
    code = input("Enter course code to delete: ")
    if code in data:
        del data[code]
        print("Course deleted successfully!")
    else:
        print("Course not found.")

def list_all_courses():
    print("List of all courses:")
    for code, details in data.items():
        print(f"{code}: {details}")

def edit():
    code = input("Enter course code to edit: ")
    if code in data:
        print("Enter new details:")
        add() 
        print("Course edited successfully!")
    else:
        print("Course not found.")


data = load_data()

while True:
    display_menu()
    user_choice = input("Enter your choice: ")

    if user_choice == 'a':
        add()
    elif user_choice == 's':
        search()
    elif user_choice == 'd':
        delete()
    elif user_choice == 'l':
        list_all_courses()
    elif user_choice == 'e':
        edit()
    elif user_choice == 'q':
        save_data()  
        print("Quitting program.")
        break
    else:
        print("Invalid input. Choose from the mentioned options.")