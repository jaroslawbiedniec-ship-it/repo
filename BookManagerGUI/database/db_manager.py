import sqlite3
from typing import List, Tuple, Optional
import os

class DatabaseManager:
    """Class for managing database connections and operations."""
    
    def __init__(self, db_name='books.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def create_tables(self):
        """Create necessary database tables if they don't exist."""
        self.create_books_table()
    
    def create_books_table(self):
        """Create the books table if it doesn't exist."""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                category TEXT,
                favorite BOOLEAN DEFAULT FALSE,
                read_count INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()
    
    def execute_query(self, query, params=()):
        """Execute a query and return the cursor."""
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor
    
    def commit(self):
        """Commit changes to the database."""
        self.conn.commit()
    
    def close(self):
        """Close the database connection."""
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
            print("Połączenie z bazą danych zamknięte.")