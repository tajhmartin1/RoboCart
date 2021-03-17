from flask import Flask, render_template
# import time
# import os
from Raspi_MotorHAT import motorTest

app = Flask(__name__)
mh = Raspi_MotorHAT(addr=0x6f)
frontRight = mh.getMotor(1)
frontLeft = mh.getMotor(2)
backLeft = mh.getMotor(3)
backRight = mh.getMotor(4)
@app.route("/")
def showCOntroller():
	return "it worked"
	# return render_template('controller.html')

@app.route("/right")
def turnRight():
    motorTest.test()
	# frontRight.setSpeed(50)
	# frontRight.run(Raspi_MotorHAT.FORWARD)
	# time.sleep(1)
	# frontRight.run(Raspi_MotorHAT.RELEASE)

if __name__ == "__main__":
	app.run()

