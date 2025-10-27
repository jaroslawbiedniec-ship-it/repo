from typing import Optional, Any

def validate_string(value: str, field_name: str, required: bool = True) -> Optional[str]:
    """Validate a string value."""
    if not value and required:
        print(f"Błąd: {field_name} jest wymagane.")
        return None
    return value

def validate_int(value: Any, field_name: str, min_value: int = None, max_value: int = None) -> Optional[int]:
    """Validate an integer value."""
    try:
        if not value and value != 0:
            return None
            
        int_value = int(value)
        
        if min_value is not None and int_value < min_value:
            print(f"Błąd: {field_name} musi być większe lub równe {min_value}.")
            return None
            
        if max_value is not None and int_value > max_value:
            print(f"Błąd: {field_name} musi być mniejsze lub równe {max_value}.")
            return None
            
        return int_value
    except ValueError:
        print(f"Błąd: {field_name} musi być liczbą całkowitą.")
        return None