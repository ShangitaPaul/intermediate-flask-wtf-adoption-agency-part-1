"""Create model for adopt app."""
"""This code defines a Pet model with columns representing various attributes of an adoptable pet. The image_url method returns either the specific photo URL of the pet or a generic image URL if no specific photo is available. The connect_db function is used to connect the database to a Flask app."""

from flask_sqlalchemy import SQLAlchemy

# Define a generic image URL for pets without a specific photo
GENERIC_IMAGE = https://www.clipartbest.com/cliparts/di7/on9/di7on9X4T.png


# Create a SQLAlchemy instance
db = SQLAlchemy()

# Define the Pet model
class Pet(db.Model):
    """Adoptable pet model."""

    # Set the table name in the database
    __tablename__ = "pets"

    # Define columns for the Pet model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return image URL for pet -- bespoke or generic."""
        # Return the specific photo URL if available, otherwise return the generic image URL
        return self.photo_url or GENERIC_IMAGE

# Define a function to connect the database to the Flask app
def connect_db(app):
    """Connect this database to the provided Flask app.

    You should call this in your Flask app.
    """
    # Set the Flask app for the database instance
    db.app = app
    # Initialize the database with the Flask app
    db.init_app(app)
