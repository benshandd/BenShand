from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config  # config now moved to its own file

app = Flask(__name__)
app.config.from_object(Config)  # applying all config to app
db = SQLAlchemy(app)

import models

@app.route("/")
def home():
        return render_template("home.html")


#route for about page
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/our_stores")
def our_stores():
    return render_template("our_stores.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/terms_of_service")
def terms_of_service():
    return render_template("terms_of_service.html")


@app.route("/refund_policy")
def refund_policy():
    return render_template("refund_policy.html")


@app.route("/work_with_us")
def work_with_us():
    return render_template("work_with_us.html")

#######################################
@app.route("/shop")
def shop():
    all_products = models.Products.query.order_by(models.Products.id).all()
    return render_template("shop.html",all_products=all_products)



@app.route('/products/<id>')
def separate_products(id):
    sep= models.Products.query.filter_by(id=id).first_or_404()
    return render_template('separate_products.html', sep=sep)


#route for sell page
@app.route("/sell")
def sell():
    return render_template("sell.html")

@app.route("/search")
def search():
    return render_template("search.html")

#reroutes 404 errrors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
