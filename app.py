from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')

@app.route('/', methods=['GET'])
def form():
    return render_template('form.html', moviesTitle = df['Title'])

@app.route('/risultati', methods=['GET'])
def risultati():
    filmInput = request.args.get('filmInput')
    film = df[df.Title == filmInput]
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)