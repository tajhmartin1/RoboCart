from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

num=5
@app.route('/test', methods =['POST'])
def update():
    num = 2
@app.route("/")
def showController():
	return render_template('controller.html', x=num)
if __name__ =="__main__":
	socketio.run(app)

@socketio.on('connect')
def connect():
    print("client has connected")
    # power up the robot