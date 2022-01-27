
from tkinter import CASCADE
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey, PrimaryKeyConstraint 

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.Text,
                     nullable=False)

    species = db.Column(db.Text,
                     nullable=False)

    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        """Show info about pet."""
        p = self
        return f'<Pet {p.name} {p.species} {p.age} {p.available} >'