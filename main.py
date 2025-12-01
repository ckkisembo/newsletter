from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/schoolproject")
def donate():
    return render_template("donate.html")

@app.route("/shoutouts")
def shoutouts():
    return render_template("shoutouts.html")

@app.route("/spin")
def spin():
    return render_template("spin.html")

@app.route("/awards")
def awards():
    return render_template("awards.html")

@app.route("/katale")
def katale():
    return render_template("katale.html")

@app.route("/news")
def notice_board():
    return render_template("news.html")

@app.route("/lifestyle")
def lifestyle():
    return render_template("lifestyle.html")

@app.route("/reunion")
def reunion():
    return render_template("reunion.html")

if __name__ == '__main__':
    app.run(debug=True)