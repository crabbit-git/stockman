from flask import Blueprint, render_template, request, redirect
from models.manufacturer import Manufacturer

from repositories import manufacturer_repository, product_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

# Manufacturer index (list all manufacturers):
@manufacturers_blueprint.route("/manufacturers")
def list_manufacturers():
    return render_template("manufacturers/index.html", manufacturers = manufacturer_repository.select_all())

# Go to form to add new manufacturer:
@manufacturers_blueprint.route("/manufacturers/add", methods=['GET'])
def goto_add_manufacturer():
    return render_template("manufacturers/add.html")

# Constructor to create new manufacturer from form input:
@manufacturers_blueprint.route("/manufacturers", methods=['POST'])
def construct_manufacturer():
    manufacturer_repository.save(
        Manufacturer(
            request.form['name'],
            request.form['country']
        )
    )
    return redirect("/manufacturers")

# Show manufacturer detail:
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['GET'])
def manufacturer_detail(id):
    selected_manufacturer = manufacturer_repository.select(id)
    return render_template(
        "manufacturers/detail.html",
        manufacturer = selected_manufacturer,
        products = product_repository.select_all_by_manufacturer(selected_manufacturer)
    )

# Go to form to edit manufacturer:
@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def goto_edit_manufacturer(id):
    return render_template(
        "manufacturers/edit.html",
        manufacturer = manufacturer_repository.select(id)
    )

# Constructor to overwrite existing manufacturer with new version with same table ID:
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['POST'])
def edit_manufacturer(id):
    manufacturer_repository.update(
        Manufacturer(
            request.form['name'],
            request.form['country'],
            id
        )
    )
    return redirect("/manufacturers")

# Destroy a given manufacturer record:
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")
