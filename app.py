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
    path = os.path.abspath("static/contest")
    groupedSongs = V.getSongs(path)
    return render_template('valley.html', groups=groupedSongs)


@app.route('/valley/<song>')
def valleySong(song):
    path = os.path.abspath("static/contest/{}".format(song))
    pages = ["contest/{}/{}".format(song, x) for x in V.getPages(path)]
    mp3s = V.getMp3Files(path)
    mp3urls = ["contest/{}/{}".format(song, x) for x in mp3s]
    if not mp3s:
       mp4s = V.getMp4Files(path)
       mp4urls = ["contest/{}/{}".format(song, x) for x in mp4s]
       # Only render first video in list (assumes 1 video per song/folder)
       return render_template('video.html', video=mp4urls[0])
    return render_template('song.html', pages=pages, mp3s=mp3s, mp3urls=mp3urls)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    manager.run()
