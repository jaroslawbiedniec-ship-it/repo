"""User model for Book Manager."""

class User:
    """Represents a user in the system."""
    
    def __init__(self, id=None, username="", email="", favorite_categories=None):
        """Initialize a new User."""
        self.id = id
        self.username = username
        self.email = email
        self.favorite_categories = favorite_categories or []
    
    def to_dict(self):
        """Convert user to dictionary."""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "favorite_categories": self.favorite_categories
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a User from dictionary."""
        return cls(
            id=data.get("id"),
            username=data.get("username", ""),
            email=data.get("email", ""),
            favorite_categories=data.get("favorite_categories", [])
        )