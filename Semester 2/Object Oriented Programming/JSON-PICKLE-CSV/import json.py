import pickle

DATA_FILE = 'courses_data.pkl'

def save_data():
    # Save courses data to a pickle file
    with open(DATA_FILE, 'wb') as file:
        pickle.dump(courses_data, file)

def load_data():
    # Load courses data from a pickle file
    try:
        with open(DATA_FILE, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}
def display_menu():
    print("\nMenu:")
    print("a) Add")
    print("s) Search")
    print("d) Delete")
    print("l) List All")
    print("e) Edit")
    print("q) Quit")

def add_course():
    code = input("Enter course code (max 8 characters): ")
    title = input("Enter course title (max 40 characters): ")
    credits = input("Enter credits hour: ")
    semester = input("Enter default semester: ")
    course_type = input("Enter course type (core or elective): ")

    courses_data[code] = {
        'title': title,
        'credits': credits,
        'semester': semester,
        'type': course_type
    }
    print("Course added successfully!")

def search_course():
    code = input("Enter course code to search: ")
    if code in courses_data:
        print("Course found:")
        print(courses_data[code])
    else:
        print("Course not found.")

def delete_course():
    code = input("Enter course code to delete: ")
    if code in courses_data:
        del courses_data[code]
        print("Course deleted successfully!")
    else:
        print("Course not found.")

def list_all_courses():
    print("List of all courses:")
    for code, details in courses_data.items():
        print(f"{code}: {details}")

def edit_course():
    code = input("Enter course code to edit: ")
    if code in courses_data:
        print("Enter new details:")
        add_course()  # Reusing the add_course function for simplicity
        print("Course edited successfully!")
    else:
        print("Course not found.")

# Load existing data (if any) at the start
courses_data = load_data()

while True:
    display_menu()
    user_choice = input("Enter your choice: ")

    if user_choice == 'a':
        add_course()
    elif user_choice == 's':
        search_course()
    elif user_choice == 'd':
        delete_course()
    elif user_choice == 'l':
        list_all_courses()
    elif user_choice == 'e':
        edit_course()
    elif user_choice == 'q':
        save_data()  # Save data before quitting
        print("Quitting program. Goodbye!")
        break
    else:
        print("Invalid input. Choose from the mentioned options.")
