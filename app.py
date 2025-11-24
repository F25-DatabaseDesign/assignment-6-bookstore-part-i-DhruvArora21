from flask import Flask, render_template, request

app = Flask(__name__)

categories = [
    {"id": 1, "name": "Autobiographies"},
    {"id": 2, "name": "History"},
    {"id": 3, "name": "Tournaments"},
    {"id": 4, "name": "Players"},
]

books = [
    {
        "title": "Messi: The Autobiography",
        "author": "Lionel Messi",
        "isbn": "9780000000001",
        "price": 18.99,
        "categoryId": 1,
        "image": "messi.jpg",
    },
    {
        "title": "Neymar: The Prince",
        "author": "Zlatan Ibrahimović",
        "isbn": "9780000000002",
        "price": 14.99,
        "categoryId": 1,
        "image": "neymar.jpg",
    },
    {
        "title": "My Turn",
        "author": "Johan Cruyff",
        "isbn": "9780000000003",
        "price": 16.50,
        "categoryId": 1,
        "image": "cruyff.jpg",
    },
    {
        "title": "El Diego",
        "author": "Diego Maradona",
        "isbn": "9780000000004",
        "price": 13.99,
        "categoryId": 1,
        "image": "maradona.jpg",
    },
    {
        "title": "The Maestro",
        "author": "Iniesta",
        "isbn": "9780000000059",
        "price": 13.99,
        "categoryId": 1,
        "image": "iniesta.jpg",
    },

    # History (categoryId 2)
    {
        "title": "Inverting the Pyramid",
        "author": "Jonathan Wilson",
        "isbn": "9780000000011",
        "price": 17.99,
        "categoryId": 2,
        "image": "history4.jpg",
    },
    {
        "title": "The Ball is Round",
        "author": "David Goldblatt",
        "isbn": "9780000000012",
        "price": 19.99,
        "categoryId": 2,
        "image": "history3.jpg",
    },
    {
        "title": "A People's History",
        "author": "Mikceal Correia",
        "isbn": "9780000000013",
        "price": 11.99,
        "categoryId": 2,
        "image": "history1.jpg",
    },
    {
        "title": "History of Soccer",
        "author": "Kenny Abdo",
        "isbn": "9780000000014",
        "price": 15.50,
        "categoryId": 2,
        "image": "history2.jpg",
    },

    # Tournaments (categoryId 3)
    {
        "title": "The FIFA World Cup",
        "author": "FIFA",
        "isbn": "9780000000021",
        "price": 21.99,
        "categoryId": 3,
        "image": "worldcup.jpg",
    },
    {
        "title": "Champions League Dream",
        "author": "Rafa Benitez",
        "isbn": "9780000000022",
        "price": 18.25,
        "categoryId": 3,
        "image": "cl.jpg",
    },
    {
        "title": "Premier League: A History in 10 Matches",
        "author": "Jim White",
        "isbn": "9780000000023",
        "price": 17.40,
        "categoryId": 3,
        "image": "prem.jpg",
    },
    {
        "title": "Fear and Loathing in LaLiga",
        "author": "Sid Lowe",
        "isbn": "9780000000024",
        "price": 16.99,
        "categoryId": 3,
        "image": "laliga.jpg",
    },

    # Players (categoryId 4)
    {
        "title": "Gods of Soccer",
        "author": "Roger Bennet",
        "isbn": "9780000000031",
        "price": 15.99,
        "categoryId": 4,
        "image": "players1.jpg",
    },
    {
        "title": "Stars of Football",
        "author": "Rodolphe Gaudin",
        "isbn": "9780000000032",
        "price": 14.99,
        "categoryId": 4,
        "image": "players2.jpg",
    },
    {
        "title": "Stars of Football",
        "author": "Rodolphe Gaudin",
        "isbn": "9780000000033",
        "price": 12.99,
        "categoryId": 4,
        "image": "players3.jpg",
    },
    {
        "title": "Greatest Ever Footballers",
        "author": "Greatest Ever",
        "isbn": "9780000000034",
        "price": 13.99,
        "categoryId": 4,
        "image": "players4.jpg",
    },
]


@app.route('/')
def home():
    return render_template("index.html", categories=categories)


@app.route('/category')
def category():
    # URL looks like: /category?category=2
    category_id = int(request.args.get("category", 1))

    # filter dicts by categoryId
    selected_books = [b for b in books if b["categoryId"] == category_id]

    return render_template(
        "category.html",
        selectedCategory=category_id,
        categories=categories,
        books=selected_books
    )


@app.errorhandler(Exception)
def handle_error(e):
    return render_template('error.html', error=e, categories=categories)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
