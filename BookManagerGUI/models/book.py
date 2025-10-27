from dataclasses import dataclass
from typing import Dict, Any, Tuple

@dataclass
class Book:
    """Class representing a book."""
    title: str
    author: str
    year: int
    category: str
    id: int = None
    favorite: bool = False
    read_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert book to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'category': self.category,
            'favorite': self.favorite,
            'read_count': self.read_count
        }

    @classmethod
    def from_row(cls, row: Tuple) -> 'Book':
        """Create a Book object from a database row."""
        return cls(
            id=row[0],
            title=row[1],
            author=row[2],
            year=row[3],
            category=row[4],
            favorite=bool(row[5]),
            read_count=row[6]
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Book':
        """Create a Book object from a dictionary."""
        return cls(
            id=data.get('id'),
            title=data['title'],
            author=data['author'],
            year=data.get('year'),
            category=data.get('category'),
            favorite=data.get('favorite', False),
            read_count=data.get('read_count', 0)
        )