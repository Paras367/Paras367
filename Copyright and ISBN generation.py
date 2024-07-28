import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import re
from datetime import datetime

class CopyrightISBNApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Copyright and ISBN Generation App")
        self.root.geometry("700x600")

        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.configure('TFrame', background='#f5f5f5')
        style.configure('TLabel', background='#f5f5f5', font=('Helvetica', 12))
        style.configure('TButton', font=('Helvetica', 12))
        style.configure('TEntry', font=('Helvetica', 12))

        self.frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.frame.pack(fill="both", expand=True)

        self.title_label = ttk.Label(self.frame, text="Title:")
        self.title_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.title_entry = ttk.Entry(self.frame, width=40)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        self.author_label = ttk.Label(self.frame, text="Author:")
        self.author_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.author_entry = ttk.Entry(self.frame, width=40)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)

        self.publisher_label = ttk.Label(self.frame, text="Publisher:")
        self.publisher_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.publisher_entry = ttk.Entry(self.frame, width=40)
        self.publisher_entry.grid(row=2, column=1, padx=10, pady=5)

        self.year_label = ttk.Label(self.frame, text="Year of Publication:")
        self.year_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.year_entry = ttk.Entry(self.frame, width=40)
        self.year_entry.grid(row=3, column=1, padx=10, pady=5)

        self.generate_button = ttk.Button(self.frame, text="Generate Copyright & ISBN", command=self.generate_info)
        self.generate_button.grid(row=4, columnspan=2, pady=20)

        self.result_text = tk.Text(self.frame, width=70, height=15, wrap=tk.WORD, font=('Helvetica', 12))
        self.result_text.grid(row=5, columnspan=2, padx=10, pady=10)

    def generate_info(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()
        year = self.year_entry.get()

        if not title or not author or not publisher or not year:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        if not re.match(r"^\d{4}$", year):
            messagebox.showwarning("Input Error", "Year must be a four-digit number.")
            return

        copyright_statement = self.generate_copyright(author, year)
        isbn10, isbn13 = self.generate_isbn()

        result = f"Title: {title}\nAuthor: {author}\nPublisher: {publisher}\nYear: {year}\n\n"
        result += f"Copyright: {copyright_statement}\nISBN-10: {isbn10}\nISBN-13: {isbn13}"

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def generate_copyright(self, author, year):
        return f"© {year} {author}. All rights reserved."

    def generate_isbn(self):
        isbn_base = ''.join(str(random.randint(0, 9)) for _ in range(9))
        check_digit10 = self.calculate_isbn10_check_digit(isbn_base)
        isbn10 = isbn_base + check_digit10

        isbn_base13 = '978' + isbn_base
        check_digit13 = self.calculate_isbn13_check_digit(isbn_base13)
        isbn13 = isbn_base13 + check_digit13

        return isbn10, isbn13

    def calculate_isbn10_check_digit(self, isbn_base):
        total = sum((i + 1) * int(num) for i, num in enumerate(isbn_base))
        remainder = total % 11
        return 'X' if remainder == 10 else str(remainder)

    def calculate_isbn13_check_digit(self, isbn_base13):
        total = sum((3 if i % 2 else 1) * int(num) for i, num in enumerate(isbn_base13))
        remainder = total % 10
        return str((10 - remainder) % 10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CopyrightISBNApp(root)
    root.mainloop()
