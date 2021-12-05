from flask import Flask, request, jsonify, render_template, session
from src.Grammar import Grammar
from src.Expression import Expression
from src.CYK import CYK

app = Flask(__name__, template_folder="views")
app.secret_key = 'secret'


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    _file = request.files["file"].read().decode("utf-8")
    _file = _file.splitlines()

    grammar = Grammar(_file)
    grammar.load()
    session["grammar"] = grammar.get()

    return render_template("show.html", grammar=grammar.get())


@app.route("/verify", methods=["POST"])
def verify():
    cyk = CYK()
    cyk.generateTable(session.get("grammar", None),
                        request.form["expression"])

    return render_template("verify.html", table=cyk.get(), verify=cyk.verify())


if __name__ == "__main__":
    app.run()
