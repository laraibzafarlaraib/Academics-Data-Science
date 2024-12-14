import sqlite3
from datetime import datetime, timedelta
conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS members (membership_number TEXT PRIMARY KEY,full_name TEXT,address TEXT,contact_number TEXT,category TEXT,membership_start_date TEXT,membership_expiry_date TEXT,membership_closing_date TEXT,fine_paid REAL)''')
conn.commit()
#c.execute('create table circulation (serial_number text, membership_number text, accession_number text, issue_date text, return_date text) ')
#conn.commit()

def add_member():
    membership_number = input("Enter membership number: ")
    full_name = input("Enter member's full name: ")
    address = input("Enter member's address: ")
    contact_number = input("Enter member's contact number: ")
    category = input("Enter member's category (A, B, C, or M): ").upper()
    membership_start_date = input("Enter membership start date (YYYY-MM-DD): ")
    if category == 'A':
        membership_expiry_date = (datetime.strptime(membership_start_date, "%Y-%m-%d") + timedelta(days=1825)).strftime("%Y-%m-%d")
        max_books_allowed = 10
    elif category == 'B':
        membership_expiry_date = (datetime.strptime(membership_start_date, "%Y-%m-%d") + timedelta(days=1095)).strftime("%Y-%m-%d")
        max_books_allowed = 7
    elif category == 'C':
        membership_expiry_date = (datetime.strptime(membership_start_date, "%Y-%m-%d") + timedelta(days=365)).strftime("%Y-%m-%d")
        max_books_allowed = 3
    elif category == 'M':
        membership_expiry_date = (datetime.strptime(membership_start_date, "%Y-%m-%d") + timedelta(days=365)).strftime("%Y-%m-%d")
        max_books_allowed = 5
    else:
        print("Invalid category. Please choose from A, B, C, or M.")
        return

    c.execute('''INSERT INTO members VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (membership_number, full_name, address, contact_number, category, membership_start_date, membership_expiry_date, None, 0))
    conn.commit()
    print("Member added successfully!")
def update_closing_date():
    membership_number = input("Enter membership number to update closing date: ")
    closing_date = input("Enter closing date (YYYY-MM-DD) or leave blank for active membership: ")

    c.execute('''UPDATE members SET membership_closing_date=? WHERE membership_number=?''', (closing_date, membership_number))
    conn.commit()
    print("Closing date updated successfully!")

def extend_expiry_date():
    membership_number = input("Enter membership number to extend expiry date: ")
    days_to_extend = int(input("Enter days to extend membership expiry date: "))

    c.execute('''SELECT membership_expiry_date FROM members WHERE membership_number=?''', (membership_number,))
    current_expiry_date = c.fetchone()[0]
    new_expiry_date = (datetime.strptime(current_expiry_date, "%Y-%m-%d") + timedelta(days=days_to_extend)).strftime("%Y-%m-%d")

    c.execute('''UPDATE members SET membership_expiry_date=? WHERE membership_number=?''', (new_expiry_date, membership_number))
    conn.commit()
    print("Expiry date extended successfully!")

while True:
    print("\nMenu:")
    print("a) Add Member, u) Update Closing Date, e) Extend Expiry Date, q) Quit")
    choice = input("Enter your choice: ").lower()

    if choice == 'a':
        add_member()
    elif choice == 'u':
        update_closing_date()
    elif choice == 'e':
        extend_expiry_date()
    elif choice == 'q':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid input. Please choose from the options.")
