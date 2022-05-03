from flask import Blueprint, render_template, request
from models.manufacturer import Manufacturer

from repositories import manufacturer_repository, product_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

# Manufacturer index (list all manufacturers):
@manufacturers_blueprint.route("/manufacturers")
def list_manufacturers():
    return render_template(
        "manufacturers/index.html",
        page = "Manufacturers",
        manufacturers = manufacturer_repository.select_all()
    )

# Go to form to add new manufacturer:
@manufacturers_blueprint.route("/manufacturers/add", methods=['GET'])
def goto_add_manufacturer():
    return render_template(
        "manufacturers/add.html",
        page = "New Manufacturer"
    )

# Constructor to create new manufacturer from form input:
@manufacturers_blueprint.route("/manufacturers", methods=['POST'])
def construct_manufacturer():
    return render_template(
        "manufacturers/added.html",
        page = "Created",
        manufacturer = manufacturer_repository.save(
            Manufacturer(
                request.form['name'],
                request.form['country']
            )
        )
    )

# Show manufacturer detail:
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['GET'])
def manufacturer_detail(id):
    selected_manufacturer = manufacturer_repository.select(id)
    return render_template(
        "manufacturers/detail.html",
        manufacturer = selected_manufacturer,
        products = product_repository.select_all(selected_manufacturer)
    )

# Go to form to edit manufacturer:
@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def goto_edit_manufacturer(id):
    return render_template(
        "manufacturers/edit.html",
        page = "Editing",
        manufacturer = manufacturer_repository.select(id)
    )

# Overwrite existing manufacturer with new version with same table ID:
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['POST'])
def edit_manufacturer(id):
    manufacturer_repository.update(
        Manufacturer(
            request.form['name'],
            request.form['country'],
            id
        )
    )
    return render_template(
        "manufacturers/updated.html",
        page = "Updated",
        manufacturer = manufacturer_repository.select(id),
        edit_type = "Manufacturer details"
    )

# Destroy a given manufacturer record if the manu has no products in the db,
# otherwise returns a failure message:
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    deletion_attempt = manufacturer_repository.delete(id)
    if deletion_attempt is not None:
        return render_template(
            "manufacturers/deletion-success.html",
            page = "Deleted",
            manufacturer_name = deletion_attempt,
        )
    else:
        return render_template(
            "manufacturers/deletion-failed.html",
            page = "Deletion failed",
            manufacturer = manufacturer_repository.select(id)
        )
