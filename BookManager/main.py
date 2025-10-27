"""Main entry point for the Book Manager application."""
from ui.book_ui import BookUI

def main():
    """Run the Book Manager application."""
    app = BookUI()
    app.run()

if __name__ == "__main__":
    main()