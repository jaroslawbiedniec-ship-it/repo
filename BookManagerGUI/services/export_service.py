"""Export service for Book Manager."""
import json
from typing import List, Dict, Any
from ..utils.file_operations import save_json

class ExportService:
    """Service for exporting book data to various formats."""
    
    @staticmethod
    def export_to_json(books: List[Dict[str, Any]], filename: str) -> bool:
        """Export books to a JSON file."""
        return save_json(books, filename)
    
    @staticmethod
    def export_to_csv(books: List[Dict[str, Any]], filename: str) -> bool:
        """Export books to a CSV file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # Write header
                headers = ["id", "title", "author", "year", "category", "favorite", "read_count"]
                f.write(','.join(headers) + '\n')
                
                # Write data
                for book in books:
                    row = [
                        str(book.get('id', '')),
                        f'"{book.get("title", "")}"',
                        f'"{book.get("author", "")}"',
                        str(book.get('year', '')),
                        f'"{book.get("category", "")}"',
                        str(book.get('favorite', False)).lower(),
                        str(book.get('read_count', 0))
                    ]
                    f.write(','.join(row) + '\n')
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False