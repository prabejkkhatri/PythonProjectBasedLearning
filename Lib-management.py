import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class LibraryManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.books = {}

        self.label_title = tk.Label(master, text="Library Management System", font=("Helvetica", 16))
        self.label_title.grid(row=0, column=0, columnspan=4, pady=10)

        self.label_book_title = tk.Label(master, text="Book Title:")
        self.label_book_title.grid(row=1, column=0, padx=10, sticky="e")
        self.entry_book_title = tk.Entry(master)
        self.entry_book_title.grid(row=1, column=1, padx=10, sticky="w")

        self.label_author = tk.Label(master, text="Author:")
        self.label_author.grid(row=2, column=0, padx=10, sticky="e")
        self.entry_author = tk.Entry(master)
        self.entry_author.grid(row=2, column=1, padx=10, sticky="w")

        self.label_genre = tk.Label(master, text="Genre:")
        self.label_genre.grid(row=3, column=0, padx=10, sticky="e")
        self.entry_genre = tk.Entry(master)
        self.entry_genre.grid(row=3, column=1, padx=10, sticky="w")

        self.label_quantity = tk.Label(master, text="Quantity:")
        self.label_quantity.grid(row=4, column=0, padx=10, sticky="e")
        self.entry_quantity = tk.Entry(master)
        self.entry_quantity.grid(row=4, column=1, padx=10, sticky="w")

        self.button_add_book = tk.Button(master, text="Add Book", command=self.add_book)
        self.button_add_book.grid(row=5, column=0, columnspan=2, pady=10)

        self.label_search = tk.Label(master, text="Search Book:")
        self.label_search.grid(row=6, column=0, padx=10, sticky="e")
        self.entry_search = tk.Entry(master)
        self.entry_search.grid(row=6, column=1, padx=10, sticky="w")

        self.button_search = tk.Button(master, text="Search", command=self.search_book)
        self.button_search.grid(row=7, column=0, columnspan=2, pady=10)

        self.table = ttk.Treeview(master, columns=("Title", "Author", "Genre", "Quantity", "Available"))
        self.table.heading("#0", text="ID")
        self.table.column("#0", width=60)
        self.table.heading("Title", text="Title")
        self.table.heading("Author", text="Author")
        self.table.heading("Genre", text="Genre")
        self.table.heading("Quantity", text="Quantity")
        self.table.heading("Available", text="Available")
        self.table.grid(row=1, column=2, rowspan=7, columnspan=3, padx=10, sticky="nsew")

        self.update_table()

        master.bind("", self.resize_table)

    def resize_table(self, event):
        table_width = event.width - 200  # Adjust for other widgets
        self.table.column("Title", width=int(table_width * 0.3))
        self.table.column("Author", width=int(table_width * 0.2))
        self.table.column("Genre", width=int(table_width * 0.2))
        self.table.column("Quantity", width=int(table_width * 0.1))
        self.table.column("Available", width=int(table_width * 0.2))

    def add_book(self):
        title = self.entry_book_title.get()
        author = self.entry_author.get()
        genre = self.entry_genre.get()
        quantity = self.entry_quantity.get()
        if title and author and genre and quantity:
            self.books[title] = {"Author": author, "Genre": genre, "Quantity": int(quantity),
                                 "Available": int(quantity)}
            self.update_table()
            messagebox.showinfo("Success", "Book added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter all book details.")

    def search_book(self):
        title = self.entry_search.get()
        self.table.delete(*self.table.get_children())
        for idx, (book_title, details) in enumerate(self.books.items(), start=1):
            if book_title.lower().startswith(title.lower()) and details["Available"] > 0:
                self.table.insert("", "end", text=idx, values=(
                book_title, details["Author"], details["Genre"], details["Quantity"], details["Available"]))
        if not self.table.get_children():
            messagebox.showinfo("Book Not Found", f"No available book found starting with: {title}")

    def update_table(self):
        self.table.delete(*self.table.get_children())
        for idx, (title, details) in enumerate(self.books.items(), start=1):
            self.table.insert("", "end", text=idx, values=(
            title, details["Author"], details["Genre"], details["Quantity"], details["Available"]))

    def clear_entries(self):
        self.entry_book_title.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)
        self.entry_genre.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.resizable(False, False)
    root.geometry("800x300")  # Decrease the width of the window
    root.mainloop()


if __name__ == "__main__":
    main()
