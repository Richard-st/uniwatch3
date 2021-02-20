from flask import Flask, render_template

from flask_socketio import SocketIO





#start the app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.debug = True
socketio = SocketIO(app,logger=True, cors_allowed_origins='*')


from app import views
from app import sockets
from app import watchWatchdog
#start thumbnail creation watchdog thread
watchWatchdog.notify()


