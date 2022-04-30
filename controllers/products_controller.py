from flask import Blueprint, render_template, request, redirect
from models.product import Product

from repositories import product_repository, manufacturer_repository

products_blueprint = Blueprint("products", __name__)

# Product index (list all products):
@products_blueprint.route("/products")
def list_products():
    return render_template(
        "products/index.html",
        products = product_repository.select_all()
    )

# Go to page to add new product:
@products_blueprint.route("/products/add", methods=['GET'])
def goto_add_product():
    return render_template(
        "products/add.html",
        manufacturers = manufacturer_repository.select_all()
    )

# Constructor to create new product from form input:
@products_blueprint.route("/products", methods=['POST'])
def construct_product():
    product_repository.save(
        Product(
            request.form['name'],
            request.form['description'],
            request.form['quantity'],
            request.form['cost'],
            request.form['price'],
            manufacturer_repository.select(request.form['manufacturer_id'])
        )
    )
    return redirect("/products")

# Show product detail:
@products_blueprint.route("/products/<id>", methods = ['GET'])
def product_detail(id):
    return render_template(
        "products/detail.html",
        product = product_repository.select(id)
    )

# Go to form to edit product:
@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def goto_edit_product(id):
    return render_template(
        "products/edit.html",
        product = product_repository.select(id),
        manufacturers = manufacturer_repository.select_all()
    )

# Constructor to overwrite existing product with new version with same table ID:
@products_blueprint.route("/products/<id>", methods=['POST'])
def edit_product(id):
    product_repository.update(
        Product(
            request.form['name'],
            request.form['description'],
            request.form['quantity'],
            request.form['cost'],
            request.form['price'],
            manufacturer_repository.select(request.form['manufacturer_id']),
            id
        )
    )
    return redirect("/products")

# Destroy a given manufacturer record:
@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")
