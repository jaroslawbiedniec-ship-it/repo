from typing import List, Optional
from models.book import Book
from services.book_service import BookService

class BookUI:
    """User interface for the book management system."""
    
    def __init__(self, book_service: BookService):
        self.book_service = book_service
        
    def print_books(self, books: List[Book]):
        """Print a list of books with improved formatting."""
        if not books:
            print("Brak książek.")
            return
        
        print("\n" + "="*80)
        print(f"{'ID':^5}|{'Tytuł':^25}|{'Autor':^20}|{'Rok':^6}|{'Kategoria':^15}|{'Ulubiona':^8}|{'Odczyty':^8}")
        print("-"*80)
        
        for book in books:
            title = book.title[:22] + "..." if len(book.title) > 22 else book.title
            author = book.author[:17] + "..." if len(book.author) > 17 else book.author
            category = book.category[:12] + "..." if len(book.category) > 12 else book.category
            favorite = "Tak" if book.favorite else "Nie"
            
            print(f"{book.id:^5}|{title:^25}|{author:^20}|{book.year:^6}|{category:^15}|{favorite:^8}|{book.read_count:^8}")
        
        print("="*80)
    
    def run(self):
        """Run the main application loop."""
        while True:
            print("\nMenu:")
            print("1. Dodaj książkę")
            print("2. Szukaj książek")
            print("3. Filtruj książki")
            print("4. Oznacz jako ulubioną")
            print("5. Zwiększ licznik odczytów")
            print("6. Pokaż ulubione")
            print("7. Najczęściej czytane kategorie")
            print("8. Najczęściej występujące kategorie")
            print("9. Edytuj książkę")
            print("10. Usuń książkę")
            print("11. Eksportuj do JSON")
            print("12. Importuj z JSON")
            print("13. Wyjście")
            
            choice = input("Wybierz opcję: ")
            
            if choice == '1':
                self.add_book_ui()
            elif choice == '2':
                self.search_books_ui()
            elif choice == '3':
                self.filter_books_ui()
            elif choice == '4':
                self.mark_favorite_ui()
            elif choice == '5':
                self.increment_read_count_ui()
            elif choice == '6':
                self.show_favorites_ui()
            elif choice == '7':
                self.show_most_read_categories_ui()
            elif choice == '8':
                self.show_most_common_categories_ui()
            elif choice == '9':
                self.edit_book_ui()
            elif choice == '10':
                self.delete_book_ui()
            elif choice == '11':
                self.export_to_json_ui()
            elif choice == '12':
                self.import_from_json_ui()
            elif choice == '13':
                break
            else:
                print("Nieprawidłowa opcja.")