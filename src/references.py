from src.papers import get_papers
from src.books import get_books

def create_file():
    papers = get_papers()
    books = get_books()
    references = ""

    for paper in papers:
        references += f"@article{{{paper["key"]},\n"
        for value in paper.keys():
            if paper[value]:
                references += f"    {value} = {{{paper[value]}}},\n"
        references += f"}}\n\n"

    for book in books:
            references += f"@book{{{book["key"]},\n"
            for value in book.keys():
                if book[value]:
                    references += f"    {value} = {{{book[value]}}},\n"
            references += "}\n\n"

    with open("references.bib", "w", encoding="utf-8") as file:
        file.write(references)