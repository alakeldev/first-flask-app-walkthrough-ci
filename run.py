import os
import json
from flask import Flask, render_template, request, flash  # Import Flask Class and render_template function   and request library from flask    and function flash from flask
if os.path.exists("env.py"):
    import env

app = Flask(__name__)    # Creating Instance and store it inside variable called app ====>>>>>>the first argument of the flask class is the name of application module
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")    # Decorator app.route  decorator to wrapping functions
def index():
    return render_template("index.html")
                        #"Hello, World"     # also you can put html elements here ex: "<h1>Hello, </h1><h2>World</h2>" instead of "Hello, World"


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open ("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj

    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # print(request.form.get("name"))
        # print(request.form["email"])
        flash("Thanks {}, We have recieved your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)   # you should know that you shoud neve have debug=True when you want to submit your project to assesment or even in production application