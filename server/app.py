from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def showController():
	return render_template('controller.html')
if __name__ =="__main__":
	socketio.run(app)

@socketio.on('connect')
def connect():
    print("client has connected")
    # power up the robot