"""Flask app for the adoption app."""
"""This code defines routes for listing pets, adding a new pet, editing an existing pet, and retrieving basic pet information via an API endpoint. The code also includes comments to explain each step in the process."""

from flask import Flask, url_for, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

# Create a Flask app instance
app = Flask(__name__)

# Set a secret key for form security
app.config['SECRET_KEY'] = "abcdef"

# Configure the database URI and disable modifications tracking
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect the database to the Flask app and create all tables
connect_db(app)
db.create_all()

# Enable the Debug Toolbar with redirects interception
toolbar = DebugToolbarExtension(app)

##############################################################################

# Route to list all pets on the homepage
@app.route("/")
def list_pets():
    """List all pets."""
    # Query all pets from the database
    pets = Pet.query.all()
    # Render the template with the list of pets
    return render_template("pet_list.html", pets=pets)

# Route to add a new pet
@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""
    # Create an instance of the AddPetForm
    form = AddPetForm()

    # If the form is submitted and valid
    if form.validate_on_submit():
        # Extract form data (excluding CSRF token)
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        # Create a new Pet instance with the form data
        new_pet = Pet(**data)
        # Add the new pet to the database
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        # Redirect to the list of pets
        return redirect(url_for('list_pets'))

    else:
        # If the form is not valid, re-present the form for editing
        return render_template("pet_add_form.html", form=form)

# Route to edit an existing pet
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""
    # Query the pet with the specified ID or return a 404 error if not found
    pet = Pet.query.get_or_404(pet_id)
    # Create an instance of the EditPetForm with the pet's data
    form = EditPetForm(obj=pet)

    # If the form is submitted and valid
    if form.validate_on_submit():
        # Update the pet's information with form data
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        # Commit the changes to the database
        db.session.commit()
        flash(f"{pet.name} updated.")
        # Redirect to the list of pets
        return redirect(url_for('list_pets'))

    else:
        # If the form is not valid, re-present the form for editing
        return render_template("pet_edit_form.html", form=form, pet=pet)

# API route to get basic info about a pet in JSON format
@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""
    # Query the pet with the specified ID or return a 404 error if not found
    pet = Pet.query.get_or_404(pet_id)
    # Create a dictionary with basic pet information
    info = {"name": pet.name, "age": pet.age}
    # Return the information in JSON format
    return jsonify(info)
