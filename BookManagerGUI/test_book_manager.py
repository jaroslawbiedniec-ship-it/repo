import unittest
import os
import json
from projekt import Book, BookManager

class TestBookManager(unittest.TestCase):
    """Test cases for the BookManager class."""
    
    def setUp(self):
        """Set up test environment before each test."""
        self.test_db = 'test_books.db'
        self.manager = BookManager(self.test_db)
    
    def tearDown(self):
        """Clean up after each test."""
        self.manager.close()
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
    
    def test_add_book(self):
        """Test adding a book."""
        book_id = self.manager.add_book("Test Title", "Test Author", 2023, "Test Category")
        self.assertIsNotNone(book_id)
        
        # Test validation
        invalid_id = self.manager.add_book("", "Test Author", 2023, "Test Category")
        self.assertIsNone(invalid_id)
    
    def test_search_books(self):
        """Test searching for books."""
        self.manager.add_book("Python Programming", "John Doe", 2020, "Programming")
        self.manager.add_book("Java Basics", "Jane Smith", 2019, "Programming")
        
        results = self.manager.search_books("Python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Python Programming")
        
        results = self.manager.search_books("Programming")
        self.assertEqual(len(results), 2)
    
    def test_mark_favorite(self):
        """Test marking a book as favorite."""
        book_id = self.manager.add_book("Test Title", "Test Author", 2023, "Test Category")
        result = self.manager.mark_favorite(book_id, True)
        self.assertTrue(result)
        
        favorites = self.manager.get_favorites()
        self.assertEqual(len(favorites), 1)
        self.assertEqual(favorites[0].title, "Test Title")

if __name__ == '__main__':
    unittest.main()