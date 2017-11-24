# Valley Lutheran Choir Practice

## About the app itself
This web application is designed to help kids at Valley Lutheran
school practice their vocal parts for small and large group
contests.

This web app renders a list of all the songs at the /valley url.
Each song is a link to a /valley/<song> url which displays the
sheet music along with a player that can be started for each
of the parts.

## About how the app is built
This app is written using the python and flask framework - using
the flask-bootstrap plugin which wraps the twitter bootstrap 2.0
web templates.

In the app's static/contest folder is one folder per song. Each
folder contains a set of jpg files - one for each page of sheet
music.  Additionally there is an mp3 file in that folder, with
the piano accompaniment for each part that goes with the sheet
music.
