import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # self is main application window of type TK
        self.title("Books Management System")
        
        # the book store
        self.books = []
        self.books.append(('Raja Gidh', 'Bano Quddsia', 2000))
        self.books.append(('Hama yarann dozakh', 'Saddique Salik', 2450))
        self.books.append(('Bange Daraa', 'Allama Ibal', 3390))
        self.books.append(('Python', 'Tony', 450))
        
        # a full window frame to contain all objects
        full_window_frame = ttk.Frame(self)
        full_window_frame.grid(row=0, column=0, padx=10, pady=10)       
        
        # Title of the book
        self.book_title_label = ttk.Label(full_window_frame, text="Title")
        self.book_title_label.grid(row=0, column=0, padx=10, pady=10)

        self.book_title_var = tk.StringVar()
        self.book_title_entry = ttk.Entry(full_window_frame, width=50)
        self.book_title_entry.grid(row=0, column=1, padx=10, pady=10)
        self.book_title_entry["textvariable"] = self.book_title_var

        # Author of the book
        self.book_author_label = ttk.Label(full_window_frame, text="Author")
        self.book_author_label.grid(row=1, column=0, padx=10, pady=10)

        self.book_author_var = tk.StringVar()
        self.book_author_entry = ttk.Entry(full_window_frame, width=50)
        self.book_author_entry.grid(row=1, column=1, padx=10, pady=10)
        self.book_author_entry["textvariable"] = self.book_author_var

        # Price of the book
        self.book_price_label = ttk.Label(full_window_frame, text="Price")
        self.book_price_label.grid(row=2, column=0, padx=10, pady=10)

        self.book_price_var = tk.IntVar()
        self.book_price_entry = ttk.Entry(full_window_frame, justify="right", width=20)
        self.book_price_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.book_price_entry["textvariable"] = self.book_price_var

        # Action buttons for the book management system
        self.book_save_button = ttk.Button(full_window_frame, text="Save Book")
        self.book_save_button.grid(row=3, column=0, padx=10, pady=10)
        #bind with left mouse button
        self.book_save_button.bind('<Button-1>', self.save_book)

        self.book_show_button = ttk.Button(full_window_frame, text="Double click here to show Book by title")
        self.book_show_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        #bind with double click of left mouse button
        self.book_show_button.bind('<Double-1>', self.show_book)

    def save_book(self, event):
        self.books.append((self.book_title_var.get(), self.book_author_var.get(), self.book_price_var.get()))
        messagebox.showinfo(title="Book Save Info", message=f"Book: {self.book_title_var.get()}, {self.book_author_var.get()}, {self.book_price_var.get()} saved")

    def show_book(self, event):
        available = False
        for b in self.books:
            if b[0] == self.book_title_var.get():
                self.book_author_var.set(b[1])
                self.book_price_var.set(b[2])
                available = True
        if available == False:
            messagebox.askokcancel(title="Book Availability", message="Not available")

def main():
    App().mainloop()

main()    