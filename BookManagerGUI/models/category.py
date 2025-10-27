"""Category model for Book Manager."""

class Category:
    """Represents a book category in the system."""
    
    def __init__(self, id=None, name="", description=""):
        """Initialize a new Category."""
        self.id = id
        self.name = name
        self.description = description
    
    def to_dict(self):
        """Convert category to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Category from dictionary."""
        return cls(
            id=data.get("id"),
            name=data.get("name", ""),
            description=data.get("description", "")
        )