from flask import Flask, render_template
from src.papers import get_papers

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/papers")
def papers():
    papers = get_papers()
    return render_template("paper_list.html", papers=papers)