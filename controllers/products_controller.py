from flask import Blueprint, render_template

from repositories import product_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def list_products():
    return render_template("products/index.html", products = product_repository.select_all())

@products_blueprint.route("/products/<id>", methods = ['GET'])
def product_detail(id):
    return render_template("products/detail.html", product = product_repository.select(id))
