import os
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
    path = os.path.abspath("static/contest")
    songs = V.getSongs(path)
    return render_template('valley.html', songs=songs)


@app.route('/valley/<song>')
def valleySong(song):
    print("rendering template song.html")
    path = os.path.abspath("static/contest/{}".format(song))
    pages = ["contest/{}/{}".format(song, x) for x in V.getPages(path)]
    mp3s = V.getMp3Files(path)
    mp3urls = ["contest/{}/{}".format(song, x) for x in mp3s]
    print pages
    print mp3s
    print mp3urls
    return render_template('song.html', pages=pages, mp3s=mp3s, mp3urls=mp3urls)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    manager.run()
