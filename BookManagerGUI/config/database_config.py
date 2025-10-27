"""Database configuration for Book Manager."""

# Database settings
DATABASE_PATH = "books.db"
ENABLE_FOREIGN_KEYS = True
JOURNAL_MODE = "WAL"  # Write-Ahead Logging for better concurrency
SYNCHRONOUS = "NORMAL"  # Balance between safety and performance

# Table definitions
BOOKS_TABLE = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    category TEXT,
    favorite BOOLEAN DEFAULT 0,
    read_count INTEGER DEFAULT 0
)
"""

# Indexes
BOOK_INDEXES = [
    "CREATE INDEX IF NOT EXISTS idx_books_title ON books(title)",
    "CREATE INDEX IF NOT EXISTS idx_books_author ON books(author)",
    "CREATE INDEX IF NOT EXISTS idx_books_category ON books(category)",
    "CREATE INDEX IF NOT EXISTS idx_books_favorite ON books(favorite)"
]