from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from db import db, Books
from book_form import BookForm
from edit_form import EditForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

db.init_app(app)
Bootstrap5(app)


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Books).order_by(Books.title))
        books = result.scalars().all()
        return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        with app.app_context():
            new_book = Books(
                title=form.name.data,
                author=form.author.data,
                rating=form.rating.data
            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    with app.app_context():
        result = db.session.execute(db.select(Books).order_by(Books.title))
        books = result.scalars().all()
        book_to_update = db.session.execute(db.select(Books).where(Books.id == id)).scalar()

        if form.validate_on_submit():
            book_to_update.rating = form.rating.data
            db.session.commit()
            return redirect(url_for('home'))

    return render_template("edit.html", form=form, id=id, books=books)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
