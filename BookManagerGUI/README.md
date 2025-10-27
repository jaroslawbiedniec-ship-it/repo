# Book Manager

A comprehensive application for managing your book collection with features for tracking, categorizing, and analyzing your reading habits.

## Features

- **Book Management**: Add, edit, and delete books in your collection
- **Search & Filter**: Find books by title, author, or category
- **Favorites**: Mark books as favorites for quick access
- **Read Tracking**: Track how many times you've read each book
- **Category Analysis**: View statistics on your most read and most common book categories
- **Data Import/Export**: Backup and restore your collection using JSON files

## Requirements

- Python 3.6+
- SQLite3 (included in Python standard library)

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application with:

```
python projekt
```

### Main Menu Options

1. Add a book
2. Search books
3. Filter books
4. Mark as favorite
5. Increment read count
6. Show favorites
7. Most read categories
8. Most common categories
9. Edit book
10. Delete book
11. Export to JSON
12. Import from JSON
13. Exit

## Data Structure

Books are stored with the following attributes:
- ID (automatically assigned)
- Title
- Author
- Year
- Category
- Favorite status
- Read count

## License

This project is open source and available for personal and educational use.