import requests
from db import db, Movies
from add_form import AddForm
from edit_form import EditForm
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, redirect, url_for, request

API_KEY = "d2af927feb2f6c6622b595803f47c41f"
API_ENDPOINT = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMmFmOTI3ZmViMmY2YzY2MjJiNTk1ODAzZjQ3YzQxZiIsInN1YiI6IjY2NzFhYjU4ZTQwMmVkYTY0OGYzMDA1NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mZe0GHe_GBCsBGLr7wT2GBDzUO1Xru55zh6fJ-rdKrM"
}

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Initialize extensions
db.init_app(app)
Bootstrap5(app)


# with app.app_context():
    # db.create_all()

    # new_movie = Movies(
    #     title="Avatar The Way of Water",
    #     year=2022,
    #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #     rating=7.3,
    #     ranking=9,
    #     review="I liked the water.",
    #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movies).order_by(Movies.rating))
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    with app.app_context():
        result = db.session.execute(db.select(Movies).order_by(Movies.id))
        movies = result.scalars().all()
        movie_to_update = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()

        if form.validate_on_submit():
            movie_to_update.rating = form.rating.data
            movie_to_update.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))

    return render_template("edit.html", form=form, id=id, movie=movie_to_update)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        response = requests.get(API_ENDPOINT, params={"api_key": API_KEY, "query": title})
        data = response.json()["results"]
        return render_template("select.html", options=data, form=form)
    return render_template('add.html', form=form)


@app.route('/add/<int:movie_id>', methods=["GET", "POST"])
def add_movie(movie_id):
    if movie_id:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        response = requests.get(url, headers=headers)
        data = response.json()

        new_movie = Movies(
            title=data.get('original_title'),
            year=data.get("release_date", "0000").split('-')[0],
            img_url=f"https://image.tmdb.org/t/p/original{data.get('poster_path')}",
            description=data.get("overview"),
            rating=round(data.get("vote_average", 0.0), 1),
            ranking=0,
            review=data.get("tagline")
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)