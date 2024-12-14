import sqlite3

conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books (
                accno TEXT,
                title TEXT,
                subtitle TEXT,
                author TEXT,
                coauthors TEXT,
                pages INTEGER,
                price REAL,
                category TEXT
             )''')
conn.commit()

# Function to add a book
def add_book():
    accno = input("Enter accession number: ")
    title = input("Enter title: ")
    subtitle = input("Enter subtitle: ")
    author = input("Enter author: ")
    coauthors = input("Enter coauthors: ")
    pages = int(input("Enter number of pages: "))
    price = float(input("Enter price: "))
    category = input("Enter category (issuable/not issuable): ")

    c.execute('''INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
              (accno, title, subtitle, author, coauthors, pages, price, category))
    conn.commit()
    print("Book added successfully!")


def search_book():
    accno = input("Enter accession number to search for: ")
    c.execute('''SELECT * FROM books WHERE accno = ?''', (accno,))
    book = c.fetchone()
    if book:
        print("Book found:")
        print(book)
    else:
        print("Book not found.")


def delete_book():
    accno = input("Enter accession number to delete: ")
    c.execute('''DELETE FROM books WHERE accno = ?''', (accno,))
    conn.commit()

import sqlite3

conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books (
                accno TEXT PRIMARY KEY,
                title TEXT,
                subtitle TEXT,
                author TEXT,
                coauthors TEXT,
                pages INTEGER,
                price REAL,
                category TEXT
             )''')
conn.commit()
def add_book():
    accno = input("Enter accession number: ")
    title = input("Enter title: ")
    subtitle = input("Enter subtitle: ")
    author = input("Enter author: ")
    coauthors = input("Enter coauthors: ")
    pages = int(input("Enter number of pages: "))
    price = float(input("Enter price: "))
    category = input("Enter category (issuable/not issuable): ")

    c.execute('''INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
              (accno, title, subtitle, author, coauthors, pages, price, category))
    conn.commit()
    print("Book added successfully!")

def search_book():
    accno = input("Enter accession number to search for: ")
    c.execute('''SELECT * FROM books WHERE accno = ?''', (accno,))
    book = c.fetchone()
    if book:
        print("Book found:")
        print(book)
    else:
        print("Book not found.")

def delete_book():
    accno = input("Enter accession number to delete: ")
    c.execute('''DELETE FROM books WHERE accno = ?''', (accno,))
    conn.commit()
    print("Book deleted successfully!")

def list_books():
    c.execute('''SELECT * FROM books''')
    all_books = c.fetchall()
    if all_books:
        print("List of all books:")
        for book in all_books:
            print(book)
    else:
        print("No books found.")

def edit_book():
    accno = input("Enter accession number: ")
    title = input("Enter title: ")
    subtitle = input("Enter subtitle: ")
    author = input("Enter author: ")
    pages = int(input("Enter number of pages: "))
    price = float(input("Enter price: "))
    category = input("Enter category : ")
    c.execute('''UPDATE books
                    SET title=?, author=?, pages=?, price=?, category=?
                    WHERE accno=?''',
                  (title, author, pages, price, category, accno))
    conn.commit()
    print("Book updated")
def quit():
    print("Exiting program. Goodbye!")

while True:
    print("\nMenu:")
    print("a) Add, s) Search, d) Delete, l) List All, q) Quit e) Edit")
    choice = input("Enter your choice: ").lower()

    if choice == 'a':
        add_book()
    elif choice == 'e':
        edit_book()
    elif choice == 's':
        search_book()
    elif choice == 'd':
        delete_book()
    elif choice == 'l':
        list_books()
    elif choice == 'q':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid input. Please choose from the options.")
