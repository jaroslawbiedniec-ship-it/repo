"""Input handling utilities for the Book Manager UI."""
from typing import Optional

def get_int_input(prompt: str) -> Optional[int]:
    """Get integer input from the user with validation."""
    while True:
        try:
            value = input(prompt)
            if not value:
                return None
            result = int(value)
            if result < 0:
                print("Proszę wprowadzić liczbę dodatnią.")
                continue
            return result
        except ValueError:
            print("Proszę wprowadzić liczbę całkowitą.")