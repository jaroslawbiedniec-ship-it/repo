"""Main GUI application for Book Manager."""
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import sys
import os

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.book import Book
from services.book_service import BookService
from database.db_manager import DatabaseManager
from gui.book_frame import BookListFrame
from gui.add_book_frame import AddBookFrame


class BookManagerApp(tk.Tk):
    """Main application window for Book Manager."""
    
    def __init__(self):
        super().__init__()
        
        # Configure the main window
        self.title("Book Manager")
        self.geometry("900x600")
        self.minsize(800, 500)
        
        # Set up the database
        self.db_manager = DatabaseManager("books.db")
        self.book_service = BookService(self.db_manager)
        
        # Create the main menu
        self.create_menu()
        
        # Create the main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create the notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.book_list_frame = BookListFrame(self.notebook, self.book_service)
        self.add_book_frame = AddBookFrame(self.notebook, self.book_service, self.refresh_book_list)
        
        self.notebook.add(self.book_list_frame, text="Książki")
        self.notebook.add(self.add_book_frame, text="Dodaj książkę")
        
        # Create status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Gotowy")
        self.status_bar = ttk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Set up theme
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use a modern theme
        
    def create_menu(self):
        """Create the application menu."""
        menu_bar = tk.Menu(self)
        
        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Eksportuj do JSON", command=self.export_to_json)
        file_menu.add_command(label="Importuj z JSON", command=self.import_from_json)
        file_menu.add_separator()
        file_menu.add_command(label="Wyjście", command=self.quit)
        menu_bar.add_cascade(label="Plik", menu=file_menu)
        
        # Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Preferencje", command=self.show_preferences)
        menu_bar.add_cascade(label="Edycja", menu=edit_menu)
        
        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="O programie", command=self.show_about)
        menu_bar.add_cascade(label="Pomoc", menu=help_menu)
        
        self.config(menu=menu_bar)
    
    def refresh_book_list(self):
        """Refresh the book list."""
        self.book_list_frame.load_books()
        self.status_var.set("Lista książek zaktualizowana")
    
    def export_to_json(self):
        """Export books to JSON file."""
        # This would be implemented with a file dialog
        messagebox.showinfo("Eksport", "Funkcja eksportu będzie dostępna wkrótce")
    
    def import_from_json(self):
        """Import books from JSON file."""
        # This would be implemented with a file dialog
        messagebox.showinfo("Import", "Funkcja importu będzie dostępna wkrótce")
    
    def show_preferences(self):
        """Show preferences dialog."""
        messagebox.showinfo("Preferencje", "Okno preferencji będzie dostępne wkrótce")
    
    def show_about(self):
        """Show about dialog."""
        messagebox.showinfo("O programie", "Book Manager\nWersja 1.0\n\nAplikacja do zarządzania kolekcją książek.")


def main():
    """Run the Book Manager GUI application."""
    app = BookManagerApp()
    app.mainloop()


if __name__ == "__main__":
    main()