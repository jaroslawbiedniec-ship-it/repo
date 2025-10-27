# Book Manager API Reference

## Book Class
Reprezentuje pojedynczą książkę w systemie.

### Atrybuty
- `id`: Unikalny identyfikator książki
- `title`: Tytuł książki
- `author`: Autor książki
- `year`: Rok wydania
- `category`: Kategoria książki
- `favorite`: Status ulubionej (True/False)
- `read_count`: Licznik odczytów

### Metody
- `to_dict()`: Konwertuje książkę na słownik
- `from_row()`: Tworzy obiekt Book z wiersza bazy danych
- `from_dict()`: Tworzy obiekt Book ze słownika

## BookManager Class
Zarządza kolekcją książek w bazie danych.

### Metody
- `add_book()`: Dodaje nową książkę
- `search_books()`: Wyszukuje książki
- `filter_books()`: Filtruje książki
- `mark_favorite()`: Oznacza książkę jako ulubioną
- `increment_read_count()`: Zwiększa licznik odczytów
- `get_favorites()`: Pobiera ulubione książki
- `edit_book()`: Edytuje informacje o książce
- `delete_book()`: Usuwa książkę
- `export_to_json()`: Eksportuje dane do pliku JSON
- `import_from_json()`: Importuje dane z pliku JSON