from flask import Flask, render_template, request
from Code import func


app = Flask(__name__)

@app.route('/',methods = ['GET'])
def show_index_html():
    return render_template('index.html')

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        pay = request.form['pay']
        movies,poster,year,genre,rating,summary = func(pay)
        length =len(movies)
        return render_template('index.html', movies = movies,poster =poster,year =year,genre =genre,rating =rating,summary =summary,length = length)

if __name__ == '__main__':
    app.run( debug=True)