from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')

@app.route('/', methods=['GET'])
def risultato():
    table = df[df['Budget'].isna()].to_html()
    return render_template('risultato.html', table = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)