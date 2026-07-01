from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="threading"
)

@socketio.on("message")
def handle(msg):
    print("Mesaj:", msg)
    socketio.emit("message", msg)

@socketio.on("connect")
def connect():
    print("Bir kullanıcı bağlandı")

@socketio.on("disconnect")
def disconnect():
    print("Bir kullanıcı çıktı")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)
