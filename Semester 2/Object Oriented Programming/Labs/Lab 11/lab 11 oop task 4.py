import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect('library.db')
c = conn.cursor()
#c.execute("create table books (accno text, title text, subtitle text, author text, coauthors text, pages text, price text, category text)")
#conn.commit()

c.execute('''SELECT category, COUNT(*) as count_members
             FROM members
             WHERE membership_closing_date IS NULL AND membership_expiry_date > date('now')
             GROUP BY category''')
category_wise_active_members = c.fetchall()
print("Category-wise Active Members List:", category_wise_active_members)
c.execute('''SELECT accession_number, COUNT(*) as count_issued
             FROM circulation
             GROUP BY accession_number''')
count_each_title_issued = c.fetchall()
print("\nCount of Each Title Issued to Members:", count_each_title_issued)
c.execute('''SELECT accession_number, COUNT(*) as count_issued, SUM(price) as total_price
             FROM circulation
             JOIN books ON circulation.accession_number = books.accno
             GROUP BY accession_number''')
count_total_price_each_title = c.fetchall()
print("\nCount and Total Price of Each Title Issued to Members:", count_total_price_each_title)
c.execute('''SELECT *
             FROM members
             WHERE membership_expiry_date BETWEEN date('now') AND date('now', '+10 days')''')
memberships_expiring_soon = c.fetchall()
print("\nMemberships to be Expired in Next 10 Days:", memberships_expiring_soon)
c.execute('''SELECT title, COUNT(*) as copies
             FROM books
             GROUP BY title
             HAVING copies = 1''')
books_with_one_copy = c.fetchall()
print("\nBooks Having Only One Copy in the Library:", books_with_one_copy)
c.execute('''SELECT title, COUNT(*) as copies
             FROM books
             GROUP BY title
             HAVING copies < 5''')
books_with_less_than_5_copies = c.fetchall()
print("\nBooks Having Less Than 5 Copies in the Library:", books_with_less_than_5_copies)
c.execute('''SELECT membership_number, full_name, SUM(fine_paid) as total_fine
             FROM members
             GROUP BY membership_number''')
members_total_unpaid_fine = c.fetchall()
print("\nMembers List with Their Total Unpaid Fine:", members_total_unpaid_fine)

conn.close()
