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

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/tutoring")
def tutoring():
    return render_template('tutoring.html')

@app.route("/landing")
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)
