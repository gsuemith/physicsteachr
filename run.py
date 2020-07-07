from flask import Flask, render_template, url_for

app = Flask(__name__)

#change
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/products")
def products():
    return render_template('products.html')

@app.route("/store")
def store():
    return render_template('store.html')

if __name__ == '__main__':
    app.run(debug=True)
