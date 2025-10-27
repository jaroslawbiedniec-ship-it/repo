"""Formatting utilities for the Book Manager."""

def truncate_text(text: str, max_length: int = 20) -> str:
    """Truncate text to a maximum length and add ellipsis if needed."""
    if not text:
        return ""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."

def format_book_table_header() -> str:
    """Return a formatted header for the book table."""
    return f"{'ID':<4} | {'Tytuł':<20} | {'Autor':<20} | {'Rok':<6} | {'Kategoria':<15} | {'Ulubiona':<8} | {'Odczyty':<7}"

def format_book_table_row(book: dict) -> str:
    """Return a formatted row for the book table."""
    favorite_mark = "★" if book.get('favorite', False) else ""
    return (f"{book.get('id', 0):<4} | "
            f"{truncate_text(book.get('title', '')):<20} | "
            f"{truncate_text(book.get('author', '')):<20} | "
            f"{book.get('year', ''):<6} | "
            f"{truncate_text(book.get('category', ''), 15):<15} | "
            f"{favorite_mark:<8} | "
            f"{book.get('read_count', 0):<7}")