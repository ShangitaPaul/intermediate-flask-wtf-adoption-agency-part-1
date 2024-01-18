"""Forms for the adoption app."""
"""These forms define fields for adding and editing pets, with appropriate validators to ensure data integrity. The comments explain the purpose and validation criteria for each field in both forms."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

# Form for adding pets
class AddPetForm(FlaskForm):
    """Form for adding pets."""

    # Pet Name field with required validation
    name = StringField(
        "Pet Name",
        validators=[InputRequired()],
    )

    # Species field with choices limited to "cat", "dog", and "porcupine"
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )

    # Photo URL field, optional but must be a valid URL if provided
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    # Age field, optional, but must be an integer between 0 and 30 if provided
    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)],
    )

    # Comments field, optional, but must have a minimum length of 10 characters if provided
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

# Form for editing an existing pet
class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    # Photo URL field, optional but must be a valid URL if provided
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    # Comments field, optional, but must have a minimum length of 10 characters if provided
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    # Available field as a Boolean (checkbox) indicating pet availability
    available = BooleanField("Available?")
