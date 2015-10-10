from flask import Flask
from flask import g, session, request, url_for, flash
from flask import redirect, render_template
import fantasyprodata


app = Flask(__name__)
app.debug = True
app.secret_key = 'development'


@app.before_request
def before_request():
    g.user = None
    if 'twitter_oauth' in session:
        g.user = session['twitter_oauth']


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
