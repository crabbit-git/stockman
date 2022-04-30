from flask import Blueprint, render_template, request, redirect
from models.manufacturer import Manufacturer

from repositories import manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def list_manufacturers():
    return render_template("manufacturers/index.html", manufacturers = manufacturer_repository.select_all())

@manufacturers_blueprint.route("/manufacturers/add", methods=['GET'])
def goto_add_manufacturer():
    return render_template(
        "manufacturers/add.html",
        manufacturers = manufacturer_repository.select_all()
    )

@manufacturers_blueprint.route("/manufacturers", methods=['POST'])
def construct_manufacturer():
    manufacturer_repository.save(
        Manufacturer(
            request.form['name'],
            request.form['country']
        )
    )
    return redirect("/manufacturers")
