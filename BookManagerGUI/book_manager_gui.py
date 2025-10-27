"""
Book Manager GUI Launcher
------------------------
This script launches the graphical user interface for the Book Manager application.
"""
import sys
import os

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the GUI application
from gui.app import main

if __name__ == "__main__":
    main()