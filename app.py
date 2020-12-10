from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	return "it worked"
if __name__ =="__main__":
	app.run()

