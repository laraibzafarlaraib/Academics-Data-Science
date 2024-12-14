import sqlite3
from datetime import datetime , timedelta
conn = sqlite3.connect('library.db')
c = conn.cursor()
c.execute("Select * from circulation")
for row in c:
    print(row)
c.execute('''CREATE TABLE IF NOT EXISTS circulation (
                serial_number INTEGER PRIMARY KEY,
                membership_number TEXT,
                accession_number TEXT,
                issue_date TEXT,
                return_date TEXT
             )''')
conn.commit()

# Function to issue a book to a member
def issue_book():
    Serial_number = input("Enter a serial no :")
    membership_number = input("Enter membership number: ")
    accession_number = input("Enter accession number of the book: ")
    issue_date = datetime.now().strftime("%Y-%m-%d")
    c.execute('''INSERT INTO circulation (Serial_number, membership_number, accession_number, issue_date, return_date) VALUES (?, ?, ?, ?, ?)''',
              (Serial_number, membership_number, accession_number, issue_date, None))
    conn.commit()
    print("Book issued successfully!")

# Function to return a book by a member
def return_book():
    serial_number = input("Enter serial number of the issued book: ")
    return_date = datetime.now().strftime("%Y-%m-%d")

    c.execute('''UPDATE circulation SET return_date=? WHERE serial_number=?''', (return_date, serial_number))
    conn.commit()
    print("Book returned successfully!")

# Main program
while True:
    print("\nMenu:")
    print("i) Issue Book, r) Return Book, q) Quit")
    choice = input("Enter your choice: ").lower()

    if choice == 'i':
        issue_book()
    elif choice == 'r':
        return_book()
    elif choice == 'q':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid input. Please choose from the options.")
