import os
import sys
# Injects our external libraries from the libs directory into our system path.
# This way we can use them on gae!
sys.path.insert(0, 'libs')

from flask import Flask
from google.appengine.ext.webapp.util import run_wsgi_app
from app import views

app = Flask(__name__)

# Register the blueprint from views.py so that our app knows how to route requests.
app.register_blueprint(views.blueprint)

# This key used for encrypting user sessions.
# http://flask.pocoo.org/docs/quickstart/#sessions
SECRET_KEY = '\xddq\xa7\x00\xb0\xdb-c\xa1\xfe\x05\x10\x80t\xe9\xc4k\xbal\x0f\xae\x7f\xad7'
app.secret_key = SECRET_KEY

if __name__ == '__main__':
    run_wsgi_app(app)
