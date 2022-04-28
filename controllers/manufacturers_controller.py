from flask import Blueprint, render_template

from repositories import manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def list_manufacturers():
    return render_template("manufacturers/index.html", manufacturers = manufacturer_repository.select_all())
