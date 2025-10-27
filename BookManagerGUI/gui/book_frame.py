"""Book list frame for displaying books in the GUI."""
import tkinter as tk
from tkinter import ttk, messagebox

class BookListFrame(ttk.Frame):
    """Frame for displaying and managing the list of books."""
    
    def __init__(self, parent, book_service):
        super().__init__(parent)
        self.book_service = book_service
        self.create_widgets()
        self.load_books()
    
    def create_widgets(self):
        """Create the widgets for the book list frame."""
        # Search frame
        search_frame = ttk.Frame(self)
        search_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(search_frame, text="Wyszukaj:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(search_frame, text="Szukaj", command=self.search_books).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Wyczyść", command=self.clear_search).pack(side=tk.LEFT, padx=5)
        
        # Filter frame
        filter_frame = ttk.Frame(self)
        filter_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(filter_frame, text="Kategoria:").pack(side=tk.LEFT, padx=5)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(filter_frame, textvariable=self.category_var, width=20)
        self.category_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(filter_frame, text="Rok:").pack(side=tk.LEFT, padx=5)
        self.year_var = tk.StringVar()
        self.year_combo = ttk.Combobox(filter_frame, textvariable=self.year_var, width=10)
        self.year_combo.pack(side=tk.LEFT, padx=5)
        
        self.favorite_var = tk.BooleanVar()
        ttk.Checkbutton(filter_frame, text="Tylko ulubione", variable=self.favorite_var, 
                        command=self.filter_books).pack(side=tk.LEFT, padx=15)
        
        ttk.Button(filter_frame, text="Filtruj", command=self.filter_books).pack(side=tk.LEFT, padx=5)
        ttk.Button(filter_frame, text="Resetuj", command=self.reset_filters).pack(side=tk.LEFT, padx=5)
        
        # Book list
        list_frame = ttk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create treeview for books
        columns = ("id", "title", "author", "year", "category", "favorite", "read_count")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        # Define headings
        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Tytuł")
        self.tree.heading("author", text="Autor")
        self.tree.heading("year", text="Rok")
        self.tree.heading("category", text="Kategoria")
        self.tree.heading("favorite", text="Ulubiona")
        self.tree.heading("read_count", text="Odczyty")
        
        # Define columns
        self.tree.column("id", width=50)
        self.tree.column("title", width=200)
        self.tree.column("author", width=150)
        self.tree.column("year", width=70)
        self.tree.column("category", width=100)
        self.tree.column("favorite", width=70)
        self.tree.column("read_count", width=70)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        # Pack the treeview and scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add right-click menu
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Edytuj", command=self.edit_book)
        self.context_menu.add_command(label="Usuń", command=self.delete_book)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Oznacz jako ulubioną", command=self.mark_favorite)
        self.context_menu.add_command(label="Zwiększ licznik odczytów", command=self.increment_read_count)
        
        self.tree.bind("<Button-3>", self.show_context_menu)
        self.tree.bind("<Double-1>", self.edit_book)
    
    def load_books(self):
        """Load books from the database."""
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get all books
        books = self.book_service.get_all_books()
        
        # Insert books into the treeview
        for book in books:
            favorite = "★" if book.get('favorite', False) else ""
            self.tree.insert("", tk.END, values=(
                book.get('id', ''),
                book.get('title', ''),
                book.get('author', ''),
                book.get('year', ''),
                book.get('category', ''),
                favorite,
                book.get('read_count', 0)
            ))
        
        # Update filter comboboxes
        self.update_filter_options()
    
    def update_filter_options(self):
        """Update the filter combobox options."""
        # Get unique categories and years
        categories = set()
        years = set()
        
        books = self.book_service.get_all_books()
        for book in books:
            if book.get('category'):
                categories.add(book.get('category'))
            if book.get('year'):
                years.add(str(book.get('year')))
        
        # Update comboboxes
        self.category_combo['values'] = [""] + sorted(list(categories))
        self.year_combo['values'] = [""] + sorted(list(years))
    
    def search_books(self):
        """Search books by the search term."""
        search_term = self.search_var.get()
        if not search_term:
            self.load_books()
            return
        
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Search books
        books = self.book_service.search_books(search_term)
        
        # Insert books into the treeview
        for book in books:
            favorite = "★" if book.get('favorite', False) else ""
            self.tree.insert("", tk.END, values=(
                book.get('id', ''),
                book.get('title', ''),
                book.get('author', ''),
                book.get('year', ''),
                book.get('category', ''),
                favorite,
                book.get('read_count', 0)
            ))
    
    def clear_search(self):
        """Clear the search field and reload all books."""
        self.search_var.set("")
        self.load_books()
    
    def filter_books(self):
        """Filter books by category, year, and favorite status."""
        category = self.category_var.get()
        year = self.year_var.get()
        favorite = self.favorite_var.get()
        
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get all books
        books = self.book_service.get_all_books()
        
        # Filter books
        filtered_books = []
        for book in books:
            if category and book.get('category') != category:
                continue
            if year and str(book.get('year')) != year:
                continue
            if favorite and not book.get('favorite'):
                continue
            filtered_books.append(book)
        
        # Insert filtered books into the treeview
        for book in filtered_books:
            favorite = "★" if book.get('favorite', False) else ""
            self.tree.insert("", tk.END, values=(
                book.get('id', ''),
                book.get('title', ''),
                book.get('author', ''),
                book.get('year', ''),
                book.get('category', ''),
                favorite,
                book.get('read_count', 0)
            ))
    
    def reset_filters(self):
        """Reset all filters and reload books."""
        self.category_var.set("")
        self.year_var.set("")
        self.favorite_var.set(False)
        self.load_books()
    
    def show_context_menu(self, event):
        """Show the context menu on right-click."""
        # Select the item under the cursor
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
    
    def get_selected_book_id(self):
        """Get the ID of the selected book."""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Wybór książki", "Proszę wybrać książkę z listy.")
            return None
        
        item = selection[0]
        book_id = self.tree.item(item, "values")[0]
        return book_id
    
    def edit_book(self, event=None):
        """Edit the selected book."""
        book_id = self.get_selected_book_id()
        if book_id:
            messagebox.showinfo("Edycja", f"Edycja książki o ID {book_id} będzie dostępna wkrótce")
    
    def delete_book(self):
        """Delete the selected book."""
        book_id = self.get_selected_book_id()
        if book_id:
            confirm = messagebox.askyesno("Usuń książkę", 
                                          "Czy na pewno chcesz usunąć tę książkę?")
            if confirm:
                self.book_service.delete_book(book_id)
                self.load_books()
    
    def mark_favorite(self):
        """Mark the selected book as favorite."""
        book_id = self.get_selected_book_id()
        if book_id:
            self.book_service.mark_favorite(book_id)
            self.load_books()
    
    def increment_read_count(self):
        """Increment the read count of the selected book."""
        book_id = self.get_selected_book_id()
        if book_id:
            self.book_service.increment_read_count(book_id)
            self.load_books()