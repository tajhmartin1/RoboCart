from flask import Flask, render_template
import RPi.GPIO as GPIO          
import time
in1 = 24
in2 = 23
in3 = 17
in4 = 27
ena = 25
enb = 22
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(ena,1000)
p=GPIO.PWM(enb,1000)
p.start(25)
p.start(22)
app = Flask(__name__)
app.route("/")
def showController():
	return "it worked"
	# return render_template('controller.html')

@app.route("/forward")
def forward():
   GPIO.output(in1,GPIO.HIGH)
   GPIO.output(in2,GPIO.LOW)
   GPIO.output(in3,GPIO.HIGH)
   GPIO.output(in4,GPIO.LOW)
   time.sleep(5)
   GPIO.output(in1,GPIO.LOW)
   GPIO.output(in2,GPIO.LOW)
   GPIO.output(in3,GPIO.LOW)
   GPIO.output(in4,GPIO.LOW)
@app.route("/backward")
def backward():
   GPIO.output(in1,GPIO.LOW)
   GPIO.output(in2,GPIO.HIGH)
   GPIO.output(in3,GPIO.LOW)
   GPIO.output(in4,GPIO.HIGH)
   time.sleep(5)
   GPIO.output(in1,GPIO.LOW)
   GPIO.output(in2,GPIO.LOW)
   GPIO.output(in3,GPIO.LOW)
   GPIO.output(in4,GPIO.LOW)
if __name__ == "__main__":
	app.run()

