from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time
import os
from flask import Flask, render_template, request
 
app = Flask(__name__, static_url_path='')
mh = Raspi_MotorHAT(addr=0x6f)
frontRight = mh.getMotor(1)
frontLeft = mh.getMotor(2)
backLeft = mh.getMotor(3)
backRight = mh.getMotor(4)

speed = 100
def stop(): 

    frontRight.run(Raspi_MotorHAT.RELEASE)
    frontLeft.run(Raspi_MotorHAT.RELEASE)
    backLeft.run(Raspi_MotorHAT.RELEASE)
    backRight.run(Raspi_MotorHAT.RELEASE)
    
def initialize():
    frontRight.setSpeed(75)
    frontLeft.setSpeed(75)
    backLeft.setSpeed(75)
    backRight.setSpeed(75)
    frontRight.run(Raspi_MotorHAT.FORWARD)
    frontLeft.run(Raspi_MotorHAT.FORWARD)
    backLeft.run(Raspi_MotorHAT.BACKWARD)
    backRight.run(Raspi_MotorHAT.BACKWARD)
    time.sleep(1)
    

def forward():
    frontRight.run(Raspi_MotorHAT.FORWARD)
    frontLeft.run(Raspi_MotorHAT.FORWARD)
    backLeft.run(Raspi_MotorHAT.BACKWARD)
    backRight.run(Raspi_MotorHAT.BACKWARD)

def backward():
    frontRight.run(Raspi_MotorHAT.BACKWARD)
    frontLeft.run(Raspi_MotorHAT.BACKWARD)
    backLeft.run(Raspi_MotorHAT.FORWARD)
    backRight.run(Raspi_MotorHAT.FORWARD)


def turnLeft():
    frontRight.setSpeed(speed)
    backRight.setSpeed(speed)
    forward()

def turnRight():
    frontLeft.setSpeed(speed)
    backLeft.setSpeed(speed)
    forward()

@app.route("/")
def index():
    render_template('index/html',name = None)
    print("test")
    
    
if __name__ == "main:":
    app.run(host='0.0.0.0'. port=80, debug=True)





