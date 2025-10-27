"""Menu handling for the Book Manager application."""

class Menu:
    def display_main_menu(self):
        """Display the main menu options."""
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
        
    def get_choice(self):
        """Get user menu choice."""
        return input("Wybierz opcję: ")