from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')

@app.route('/', methods=['GET'])
def form():
    return render_template('home.html')

@app.route('/form0', methods=['GET'])
def form0():
    return render_template('form.html')

@app.route('/risultati0', methods=['GET'])
def risultati0():
    filmInput = request.args.get('filmInput')
    film = df[df.Title.str.contains(filmInput)]
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)

@app.route('/form1', methods=['GET'])
def form1():
    return render_template('form1.html')

@app.route('/risultati1', methods=['GET'])
def risultati1():
    filmInput = str(request.args.get('filmInput'))
    film = df[df.Genres.str.contains(filmInput)]
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)

@app.route('/form2', methods=['GET'])
def form2():
    moviesGenres = df[~df['Genres'].str.contains('\|')]['Genres'].to_list()
    moviesGenres = list(set(moviesGenres))
    return render_template('form2.html', moviesGenres = moviesGenres )

@app.route('/risultati2', methods=['GET'])
def risultati2():
    filmInput = str(request.args.get('filmInput'))
    film = df[df.Genres.str.contains(filmInput)]
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)

@app.route('/form3', methods=['GET'])
def form3():
    moviesGenres = df[~df['Genres'].str.contains('\|')]['Genres'].to_list()
    moviesGenres = list(set(moviesGenres))
    return render_template('form3.html', moviesGenres = moviesGenres )

@app.route('/risultati3', methods=['GET'])
def risultati3():
    filmInput = str(request.args.get('filmInput'))
    film = df[df.Genres.str.contains(filmInput)]
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)

@app.route('/form4', methods=['GET'])
def form4():
    moviesGenres = df[~df['Genres'].str.contains('\|')]['Genres'].to_list()
    moviesGenres = list(set(moviesGenres))
    return render_template('form4.html', moviesGenres = moviesGenres )

@app.route('/risultati4', methods=['GET'])
def risultati4():
    filmInput = str(request.args.get('filmInput'))
    film = df[df.Genres.str.contains(filmInput)]
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)

@app.route('/form5', methods=['GET'])
def risultato5():
    table = df[df['Budget'].isna()].to_html()
    return render_template('risultato.html', table = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)