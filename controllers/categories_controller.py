from flask import Blueprint, render_template, request, redirect
from models.category import Category

from repositories import category_repository, product_repository

categories_blueprint = Blueprint("categories", __name__)

# category index (list all categories):
@categories_blueprint.route("/categories")
def list_categories():
    return render_template(
        "categories/index.html",
        page = "Categories",
        categories = category_repository.select_all()
    )

# Go to form to add new category:
@categories_blueprint.route("/categories/add", methods=['GET'])
def goto_add_category():
    return render_template(
        "categories/add.html",
        page = "New Category"
    )

# Constructor to create new category from form input:
@categories_blueprint.route("/categories", methods=['POST'])
def construct_category():
    category_repository.save(
        Category(
            request.form['name'],
            request.form['country']
        )
    )
    return redirect("/categories")

# Show category detail:
@categories_blueprint.route("/categories/<id>", methods=['GET'])
def category_detail(id):
    selected_category = category_repository.select(id)
    return render_template(
        "categories/detail.html",
        category = selected_category,
        products = product_repository.select_all(selected_category)
    )

# Go to form to edit category:
@categories_blueprint.route("/categories/<id>/edit", methods=['GET'])
def goto_edit_category(id):
    return render_template(
        "categories/edit.html",
        page = "Editing",
        category = category_repository.select(id)
    )

# Constructor to overwrite existing category with new version with same table ID:
@categories_blueprint.route("/categories/<id>", methods=['POST'])
def edit_category(id):
    category_repository.update(
        Category(
            request.form['name'],
            request.form['country'],
            id
        )
    )
    return redirect("/categories")

# Destroy a given category record:
@categories_blueprint.route("/categories/<id>/delete", methods=['POST'])
def delete_category(id):
    category_repository.delete(id)
    return redirect("/categories")
