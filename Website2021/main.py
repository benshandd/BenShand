import sqlite3
from flask import Flask, render_template
from flask import g

app = Flask(__name__)

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


@app.route("/shop")
def shop():
        conn = sqlite3.connect('WhoCares.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Products ORDER BY id;")
        gg = c.fetchall()
        conn.close()
        return render_template("shop.html", gg=gg)


@app.route('/products/<id>')
def separate_products(id):
        conn = sqlite3.connect('WhoCares.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Products WHERE id=?;",(id,))
        get_product = c.fetchone()
        conn.close()
        return render_template("separate_products.html", get_product=get_product)


#route for sell page
@app.route("/sell")
def sell():
    return render_template("sell.html")


#reroutes 404 errrors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
