from typing import List, Optional, Tuple, Dict
from models.book import Book
from database.db_manager import DatabaseManager
import sqlite3
import json
import os
from collections import Counter

class BookService:
    """Service class for book-related operations."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    def add_book(self, title: str, author: str, year: int, category: str) -> int:
        """Add a new book to the database."""
        # Validate inputs
        if not title or not author:
            print("Błąd: Tytuł i autor są wymagane.")
            return None
            
        if not isinstance(year, int) or year < 0 or year > 9999:
            print("Błąd: Rok musi być liczbą całkowitą między 0 a 9999.")
            return None
            
        try:
            cursor = self.db_manager.execute_query('''
                INSERT INTO books (title, author, year, category)
                VALUES (?, ?, ?, ?)
            ''', (title, author, year, category or "Brak kategorii"))
            self.db_manager.commit()
            print(f"Książka '{title}' dodana pomyślnie.")
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Błąd podczas dodawania książki: {e}")
            return None
    
    def search_books(self, query: str) -> List[Book]:
        """Search for books by title, author, or category."""
        try:
            cursor = self.db_manager.execute_query('''
                SELECT * FROM books
                WHERE title LIKE ? OR author LIKE ? OR category LIKE ?
            ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
            return [Book.from_row(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Błąd podczas wyszukiwania książek: {e}")
            return []
    
    def filter_books(self, category: Optional[str] = None, 
                    year: Optional[int] = None, 
                    favorite: bool = False) -> List[Book]:
        """Filter books by category, year, and/or favorite status."""
        try:
            query = 'SELECT * FROM books WHERE 1=1'
            params = []
            if category:
                query += ' AND category = ?'
                params.append(category)
            if year:
                query += ' AND year = ?'
                params.append(year)
            if favorite:
                query += ' AND favorite = 1'
            cursor = self.db_manager.execute_query(query, params)
            return [Book.from_row(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Błąd podczas filtrowania książek: {e}")
            return []