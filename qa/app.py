import os
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def validate():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))