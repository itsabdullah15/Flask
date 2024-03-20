from flask import Flask, render_template, send_from_directory

app = Flask(__name__,static_url_path='/static', static_folder='static')


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/serve_assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('/home/abdullah/Desktop/Code/Python/Flask/03Portfolio/Portfolio/serve_assets/', filename)