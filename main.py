import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import sqlite3


class DataBase:
    def __init__(self):
        # Create or connect to the SQLite database
        conn = sqlite3.connect('library.db')
        c = conn.cursor()

        # Create the 'authors' table
        c.execute('''CREATE TABLE IF NOT EXISTS authors
                     (id INTEGER PRIMARY KEY, author TEXT)''')

        # Create the 'books' table
        c.execute('''CREATE TABLE IF NOT EXISTS books
                     (book_id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author_id INTEGER,
                     FOREIGN KEY (author_id) REFERENCES authors(id))''')

        # Commit the transaction
        conn.commit()


class LibraryManagement:
    def __init__(self):
        self.library_db = DataBase()

    def add_record(self, author=None, title=None, year=None):
        pass

    def delete_record(self, id):
        pass


class UserInterface:
    def __init__(self):
        # Create the main window
        self.root = Tk()
        self.root.title("Home library")  # Title
        self.root.geometry("800x600")  # Frame size
        # Create and add buttons
        self.create_buttons()
        # Library creation
        self.library_management = LibraryManagement()
        self.library_treeview = None
        self.create_library()
        # Book add form creation
        self.author_entry = None
        self.title_entry = None
        self.year_entry = None
        self.create_book_form()

    def create_buttons(self):
        show_library_button = Button(
            self.root,
            text="Show Library",
            command=self.show_library,
            bg='#F9F9F9', fg='black', font='Arial 16',
            width=14
        )
        show_library_button.pack(anchor=N, padx=10, pady=5)
        add_book_button = Button(
            self.root,
            text="Add a Book",
            command=self.add_book,
            bg='#F9F9F9', fg='black', font='Arial 16',
            width=14
        )
        add_book_button.pack(anchor=N, padx=10, pady=5)
        delete_book_button = Button(
            self.root,
            text="Delete a Book",
            command=self.delete_book,
            bg='#F9F9F9', fg='black', font='Arial 16',
            width=14
        )
        delete_book_button.pack(anchor=N, padx=10, pady=5)

    def create_library(self):
        self.library_treeview = ttk.Treeview(
            self.root, columns=('Author', 'Title', 'Year'), show='headings',
        )
        self.library_treeview.heading('Author', text='Author')
        self.library_treeview.heading('Title', text='Title')
        self.library_treeview.heading('Year', text='Year')
        self.library_treeview.pack(anchor=S)

    def create_book_form(self):
        book_frame = Frame(
            height=100, width=700,  # frame size
            borderwidth=1, relief=SOLID, bg='#F9F9F9'
        )
        book_frame.pack(anchor=S)

        author_label = Label(book_frame, text="Author:")
        author_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.author_entry = Entry(book_frame)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)

        title_label = Label(book_frame, text="Title:")
        title_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.title_entry = Entry(book_frame)
        self.title_entry.grid(row=2, column=1, padx=10, pady=5)

        year_label = Label(book_frame, text="Year:")
        year_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.year_entry = Entry(book_frame)
        self.year_entry.grid(row=3, column=1, padx=10, pady=5)

    def show_library(self):
        pass

    def add_book(self):
        # Check whether title field is empty
        if self.title_entry.get() == '':
            msg = 'Please, enter title name to add a book'
            tkinter.messagebox.showinfo('Warning', msg)
        else:
            self.library_management.add_record(self.author_entry.get(), self.title_entry.get(), self.year_entry.get())
            self.clear_entry_fields()

    def delete_book(self):
        if self.id_entry.get() == '':
            msg = 'Please, enter book ID to delete a book'
            tkinter.messagebox.showinfo('Warning', msg)
        else:
            print(self.id_entry.get())
            self.clear_entry_fields()

    def clear_entry_fields(self):
        self.author_entry.delete(0, 'end')
        self.title_entry.delete(0, 'end')
        self.year_entry.delete(0, 'end')

    def run(self):
        self.root.mainloop()


UserInterface().run()