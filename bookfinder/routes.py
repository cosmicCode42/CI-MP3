from flask import render_template, request, redirect, url_for
from bookfinder import app, db
from bookfinder.models import Author, Genre, Book


@app.route("/")
def home():
    # home page
    return render_template("index.html")