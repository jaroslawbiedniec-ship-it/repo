"""Import service for Book Manager."""
import csv
from typing import List, Dict, Any, Optional
from ..utils.file_operations import load_json

class ImportService:
    """Service for importing book data from various formats."""
    
    @staticmethod
    def import_from_json(filename: str) -> Optional[List[Dict[str, Any]]]:
        """Import books from a JSON file."""
        return load_json(filename)
    
    @staticmethod
    def import_from_csv(filename: str) -> Optional[List[Dict[str, Any]]]:
        """Import books from a CSV file."""
        try:
            books = []
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert types
                    book = {
                        'id': int(row.get('id', 0)),
                        'title': row.get('title', ''),
                        'author': row.get('author', ''),
                        'year': int(row.get('year', 0)),
                        'category': row.get('category', ''),
                        'favorite': row.get('favorite', '').lower() == 'true',
                        'read_count': int(row.get('read_count', 0))
                    }
                    books.append(book)
            return books
        except Exception as e:
            print(f"Error importing from CSV: {e}")
            return None