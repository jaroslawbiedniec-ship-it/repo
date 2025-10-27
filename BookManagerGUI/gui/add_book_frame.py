"""Add book frame for the Book Manager GUI."""
import tkinter as tk
from tkinter import ttk, messagebox

class AddBookFrame(ttk.Frame):
    """Frame for adding new books."""
    
    def __init__(self, parent, book_service, refresh_callback):
        super().__init__(parent)
        self.book_service = book_service
        self.refresh_callback = refresh_callback
        self.create_widgets()
    
    def create_widgets(self):
        """Create the widgets for the add book frame."""
        # Create a form for adding books
        form_frame = ttk.Frame(self, padding="20")
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(form_frame, text="Tytuł:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.title_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.title_var, width=40).grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Author
        ttk.Label(form_frame, text="Autor:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.author_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.author_var, width=40).grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Year
        ttk.Label(form_frame, text="Rok:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.year_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.year_var, width=10).grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Category
        ttk.Label(form_frame, text="Kategoria:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.category_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.category_var, width=20).grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Favorite
        self.favorite_var = tk.BooleanVar()
        ttk.Checkbutton(form_frame, text="Ulubiona", variable=self.favorite_var).grid(row=4, column=1, sticky=tk.W, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Dodaj książkę", command=self.add_book).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Wyczyść formularz", command=self.clear_form).pack(side=tk.LEFT, padx=5)
    
    def add_book(self):
        """Add a new book to the database."""
        # Validate input
        title = self.title_var.get().strip()
        author = self.author_var.get().strip()
        year_str = self.year_var.get().strip()
        category = self.category_var.get().strip()
        favorite = self.favorite_var.get()
        
        if not title:
            messagebox.showerror("Błąd", "Tytuł jest wymagany.")
            return
        
        if not author:
            messagebox.showerror("Błąd", "Autor jest wymagany.")
            return
        
        try:
            year = int(year_str) if year_str else None
        except ValueError:
            messagebox.showerror("Błąd", "Rok musi być liczbą.")
            return
        
        # Add the book
        book = {
            'title': title,
            'author': author,
            'year': year,
            'category': category,
            'favorite': favorite,
            'read_count': 0
        }
        
        success = self.book_service.add_book(book)
        
        if success:
            messagebox.showinfo("Sukces", "Książka została dodana.")
            self.clear_form()
            self.refresh_callback()
        else:
            messagebox.showerror("Błąd", "Nie udało się dodać książki.")
    
    def clear_form(self):
        """Clear the form fields."""
        self.title_var.set("")
        self.author_var.set("")
        self.year_var.set("")
        self.category_var.set("")
        self.favorite_var.set(False)