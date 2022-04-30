from flask import Blueprint, render_template, request, redirect
from models.product import Product

from repositories import product_repository, manufacturer_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products/add", methods=['GET'])
def goto_add_product():
    return render_template(
        "products/add.html",
        manufacturers = manufacturer_repository.select_all()
    )

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

@products_blueprint.route("/products")
def list_products():
    return render_template(
        "products/index.html",
        products = product_repository.select_all()
    )

@products_blueprint.route("/products/<id>", methods = ['GET'])
def product_detail(id):
    return render_template(
        "products/detail.html",
        product = product_repository.select(id)
    )
