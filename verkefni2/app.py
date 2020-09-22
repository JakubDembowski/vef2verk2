from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/a-hluti')
def ahluti():
    return render_template('kennitala.html')

@app.route('/k-tala/<kt>')
def ktalan(kt):
    summa = 0
    for item in kt:
        summa += int(item)
    return render_template('ktsum.html', kt=kt, summa=summa)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hæ %s' % escape(username)

frettir = [
    ["0", "123", "1234", "132"]
    ["1",  "123", "123", "1234"]
    ["2", "34", "gr", "t"]
    ["3", "4", "gt", "5"]
]
demo = [
    ["0", "123", "1234", "132"]
    ["1",  "123", "123", "1234"]
    ["2", "34", "gr", "t"]
    ["3", "4", "gt", "5"]
]
@app.route('/b-hluti')
def bhluti():
    return render_template("frettir.html", frettir=demo)

@app.route('/frett/<int:id>')
def news(id):
    return render_template('frett.html', frett=frettir[id], nr=id)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

@app.errorhandler(500)
def servernotfound(error):
    return render_template('servererror.html'), 500
if __name__ == '__main__':
    app.run()
