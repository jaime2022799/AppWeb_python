from werkzeug.middleware.proxy_fix import ProxyFix 
from flask import Flask

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)