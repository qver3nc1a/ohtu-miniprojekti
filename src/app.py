from flask import Flask, render_template, request, redirect, Response
from src.database import create_tables
from src.papers import add_paper, get_papers
from src.books import add_book, get_books
from src.conference import add_conference, get_conferences
from src.references import create_file

app = Flask(__name__)
create_tables()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/references-menu")
def references_menu():
    return render_template("references_menu.html")


@app.route("/references")
def references():
    papers = get_papers()
    books = get_books()
    conferences = get_conferences()
    return render_template("reference_list.html", papers=papers, books=books, conferences=conferences)

@app.route("/papers")
def papers():
    papers = get_papers()
    return render_template("paper_list.html", papers=papers)

@app.route("/books")
def books():
    books = get_books()
    return render_template("book_list.html", books=books)

@app.route("/conferences")
def conferences():
    conferences = get_conferences()
    return render_template("conference_list.html", conferences=conferences)

@app.route("/new_paper")
def new_paper():
    return render_template("new_paper.html")


@app.route("/new_book")
def new_book():
    return render_template("new_book.html")

@app.route("/new_conference")
def new_conference():
    return render_template("new_conference.html")

@app.route("/add_conference", methods=["POST"])
def add_new_conference():
    author = request.form["author"].strip()
    title = request.form["title"].strip()
    booktitle = request.form["booktitle"].strip()
    year = request.form["year"].strip()
    month = request.form["month"].strip()
    editor = request.form["editor"].strip()
    volume = request.form["volume"].strip()
    number = request.form["number"].strip()
    series = request.form["series"].strip()
    pages = request.form["pages"].strip()
    organization = request.form["organization"].strip()
    note = request.form["note"].strip()
    publisher = request.form["publisher"].strip()
    address = request.form["address"].strip()

    if not title or not author:
        return render_template(
            "new_conference.html",
            error="Otsikko ja kirjoittaja ovat pakollisia"
        )
    if year:
        try:
            year = int(year)
        except ValueError:
            return render_template(
                "new_conference.html",
                error="Vuoden täytyy olla numero"
            )
        if year < 0:
            return render_template(
                "new_conference.html",
                error="Vuosi ei voi olla negatiivinen"
            )
        if year > 2026:
            return render_template(
                "new_conference.html",
                error="Vuosi ei voi olla tulevaisuudessa"
            )

    add_conference(
        author,
        title,
        booktitle,
        year,
        month,
        editor,
        volume,
        number,
        series,
        pages,
        organization,
        note,
        publisher,
        address
    )
    return redirect("/")

@app.route("/add_paper", methods=["POST"])
def add_new_paper():
    key = request.form["key"].strip()
    author = request.form["author"].strip()
    title = request.form["title"].strip()
    journal = request.form["journal"].strip()
    year = request.form["year"].strip()
    volume = request.form["volume"].strip()
    number = request.form["number"].strip()
    pages = request.form["pages"].strip()

    if not author or not title or not year:
        return render_template(
            "new_paper.html",
            error="Tekijä, otsikko, julkaisu ja julkaisuvuosi ovat pakollisia"
        )
    try:
        year = int(year)
        if volume:
            volume = int(volume)
        if number:
            number = int(number)
    except ValueError:
        return render_template(
            "new_paper.html",
            error="Vuoden, vuosikerran ja numeron täytyy olla numeroita"
        )
    if year < 0:
        return render_template(
            "new_paper.html",
            error="Vuosi ei voi olla negatiivinen"
        )
    if year > 2026:
        return render_template(
            "new_paper.html",
            error="Vuosi ei voi olla tulevaisuudessa"
        )

    add_paper(
        key,
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
    books = get_books()
    return render_template("bibtex.html", papers=papers, books=books)

@app.route("/add_book", methods=["POST"])
def add_new_book():
    key = request.form["key"].strip()
    title = request.form["title"].strip()
    author = request.form["author"].strip()
    year = request.form["year"].strip()
    publisher = request.form["publisher"].strip()
    address = request.form["address"].strip()

    if not title or not author or not year:
        return render_template(
            "new_book.html",
            error="Otsikko, kirjoittaja ja julkaisuvuosi ovat pakollisia"
        )
    try:
        year = int(year)
    except ValueError:
        return render_template(
            "new_book.html",
            error="Vuoden täytyy olla numero"
        )
    if year < 0:
        return render_template(
            "new_book.html",
            error="Vuosi ei voi olla negatiivinen"
        )
    if year > 2026:
        return render_template(
            "new_book.html",
            error="Vuosi ei voi olla tulevaisuudessa"
        )

    add_book(
        key,
        author,
        title,
        publisher,
        year,
        address,
    )
    return redirect("/")

@app.route("/references.bib")
def create_bibtex_file():
    references = create_file()
    return Response(
        references,
        mimetype="application/x-bibtex",
        headers={"Content-Disposition": "attachment; filename=references.bib"}
    )
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
