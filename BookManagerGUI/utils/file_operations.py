"""File operation utilities for the Book Manager."""
import os
import json
from typing import Dict, List, Any

def ensure_directory_exists(directory_path: str) -> None:
    """Ensure that a directory exists, creating it if necessary."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def save_json(data: Any, filename: str, encoding: str = 'utf-8') -> bool:
    """Save data to a JSON file."""
    try:
        with open(filename, 'w', encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except (IOError, TypeError) as e:
        print(f"Error saving JSON file: {e}")
        return False

def load_json(filename: str, encoding: str = 'utf-8') -> Any:
    """Load data from a JSON file."""
    try:
        if not os.path.exists(filename):
            return None
        with open(filename, 'r', encoding=encoding) as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading JSON file: {e}")
        return None