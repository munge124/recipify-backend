from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy here to avoid circular imports
db = SQLAlchemy()

# Import models after db to ensure they can inherit `db.Model`
from .user import User
from .recipe import Recipe
from .comment import Comment

__all__ = ['db', 'User', 'Recipe', 'Comment']