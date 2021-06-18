from flask import Flask, render_template, request
from Code import func
from Code import func1
from connection import data_insert

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_index_html():
    return render_template('index.html')


@app.route('/update.html', methods=['POST'])
def show_index():
    return render_template('update.html')

@app.route('/send_data', methods=['POST'])
def get_data_from_html():
    pay = request.form['pay']
    movies, poster, year, genre, rating, summary = func(pay)
    length = len(movies)
    return render_template('index.html', movies=movies, poster=poster, year=year, genre=genre, rating=rating, summary=summary, length=length)


@app.route('/send_Genres', methods=['POST'])
def get_data():
    inp = request.form['Genres']
    movies, poster, year, genre, rating, summary = func1(inp)
    length = len(movies)
    return render_template('index.html', movies=movies, poster=poster, year=year, genre=genre, rating=rating, summary=summary, length=length)


@app.route('/Add_data', methods=['POST'])
def add_data():
    rating = request.form['rating']
    name = request.form['name']
    genre = request.form['genre']
    year = request.form['year']
    summary = request.form['summary']
    cast = request.form['cast']
    writer = request.form['writer']
    poster = request.form['trailer']
    director = request.form['director']
    data_insert(name,genre,cast,director,writer,summary,poster,year,rating)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
