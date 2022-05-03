from flask import Blueprint, render_template, request
from models.product import Product

from repositories import product_repository, manufacturer_repository, category_repository

products_blueprint = Blueprint("products", __name__)

# Product index (list all products):
@products_blueprint.route("/products")
def list_products():
    return render_template(
        "products/index.html",
        page = "All Products",
        products = product_repository.select_all()
    )

# Only in stock products:
@products_blueprint.route("/products/in-stock")
def list_in_stock():
    return render_template(
        "products/index.html",
        page = "In Stock",
        products = product_repository.select_all("in stock")
    )

# Only out of stock products:
@products_blueprint.route("/products/out-of-stock")
def list_out_of_stock():
    return render_template(
        "products/index.html",
        page = "Out Of Stock",
        products = product_repository.select_all("out of stock")
    )

# Go to page to add new product:
@products_blueprint.route("/products/add", methods=['GET'])
def goto_add_product():
    return render_template(
        "products/add.html",
        page = "New Product",
        manufacturers = manufacturer_repository.select_all(),
        categories = category_repository.select_all()
    )

# Constructor to create new product from form input:
@products_blueprint.route("/products", methods=['POST'])
def construct_product():
    return render_template(
        "products/added.html",
        page = "Created",
        product = product_repository.save(
            Product(
                request.form['name'],
                category_repository.select(request.form['category_id']),
                request.form['description'],
                request.form['quantity'],
                request.form['cost'],
                request.form['price'],
                manufacturer_repository.select(request.form['manufacturer_id'])
            )
        )
    )

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
        page = "Editing",
        product = product_repository.select(id),
        manufacturers = manufacturer_repository.select_all(),
        categories = category_repository.select_all()
    )

# Overwrite existing product with new version with same table ID:
@products_blueprint.route("/products/<id>", methods=['POST'])
def edit_product(id):
    product_repository.update(
        Product(
            request.form['name'],
            category_repository.select(request.form['category_id']),
            request.form['description'],
            product_repository.select(id).quantity,
            request.form['cost'],
            request.form['price'],
            manufacturer_repository.select(request.form['manufacturer_id']),
            id
        )
    )
    return render_template(
        "products/updated.html",
        page = "Updated",
        product = product_repository.select(id),
        edit_type = "Product details"
    )

# Update quantity only for a given product:
@products_blueprint.route("/products/<id>/count", methods=['POST'])
def count_product(id):
    product_repository.count(id, request.form['quantity'])
    return render_template(
        "products/updated.html",
        page = "Updated",
        product = product_repository.select(id),
        edit_type = "Stock"
    )

# Destroy a given product record:
@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    return render_template(
        "products/deletion-result.html",
        page = "Deleted",
        product_name = product_repository.delete(id),
        edit_type = "Product deleted"
    )
