from flask import Flask, render_template

from controllers.manufacturers_controller import manufacturers_blueprint
from controllers.products_controller import products_blueprint
from controllers.categories_controller import categories_blueprint

app = Flask(__name__)

app.register_blueprint(manufacturers_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(categories_blueprint)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
