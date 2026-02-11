from flask import Flask, render_template, request

app = Flask(__name__)







@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        value = request.value
        base = request.base

    return render_template('index.html')

app.run(debug=True)