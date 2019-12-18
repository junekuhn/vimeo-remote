from flask import Flask
from flask_socketio import SocketIO, join_room, emit
from flask_cors import CORS

app = Flask(__name__)
#app.config.from_envvar('APP_SETTINGS')
CORS(app,supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins="*", always_connect=True, ping_interval="2", ping_timeout="5", cookie=None, logger=True, engineio_logger=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

from app import routes