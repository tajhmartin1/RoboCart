from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def showCOntroller():
	return render_template('controller.html')
if __name__ == "__main__":
	app.run()
