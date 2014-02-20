import os
import sys
sys.path.insert(0, 'libs')

from flask import Flask

from google.appengine.ext.webapp.util import run_wsgi_app
from app import views

app = Flask(__name__)

app.register_blueprint(views.blueprint)

SECRET_KEY = '\xddq\xa7\x00\xb0\xdb-c\xa1\xfe\x05\x10\x80t\xe9\xc4k\xbal\x0f\xae\x7f\xad7'
app.secret_key = SECRET_KEY

if __name__ == '__main__':
    run_wsgi_app(app)
