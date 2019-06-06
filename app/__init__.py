from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

#set up default config needed by request and not used in this demo
app.config.update(dict(
  HEADERS={'Accept': 'application/json'},
  USERNAME='user',
  PASSWORD='password',
))
from app import views

