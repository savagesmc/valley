from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from valley import valley as V

from flask_script import Manager
app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())

@app.route('/valley')
def valley():
    print("rendering template valley.html")
    songs = V.getSongs("contest")
    return render_template('valley.html', songs=songs)

@app.route('/valley/<song>')
def valleySong(song):
    print("rendering template song.html")
    pages = V.getPages(song)
    return render_template('song.html', pages=pages)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    manager.run()
