from flask import Flask, render_template, request, redirect
from src.database import create_tables
from src.papers import add_paper, get_papers

app = Flask(__name__)
create_tables()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/papers")
def papers():
    papers = get_papers()
    return render_template("paper_list.html", papers=papers)


@app.route("/new_paper")
def new_paper():
    return render_template("new_paper.html")


@app.route("/add_paper", methods=["POST"])
def add_new_paper():
    author = request.form["author"].strip()
    title = request.form["title"].strip()
    journal = request.form["journal"].strip()
    year = request.form["year"].strip()
    volume = request.form["volume"].strip()
    number = request.form["number"].strip()
    pages = request.form["pages"].strip()

    if not author or not title or not journal or not year:
        return "Tekijä, otsikko, julkaisu ja julkaisuvuosi ovat pakollisia"
    try:
        year = int(year)
        volume = int(volume)
        number = int(number)
    except ValueError:
        return "Vuoden, volyymin ja numeron täytyy olla numeroita"
    if year < 0 or year > 2026:
        return "Virheellinen vuosi (täytyy olla 0 < vuosi < 2027)"

    add_paper(
        author,
        title,
        journal,
        year,
        volume,
        number,
        pages,
    )
    return redirect("/")

@app.route("/bibtex")
def bibtex():
    papers = get_papers()
    return render_template("bibtex.html")
