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
def test():
    print('it worked')
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
    frontRight.setSpeed(speed)
    time.sleep(1)
    forward()
time.sleep(10)
initialize()
time.sleep(1)
forward()
time.sleep(3)
stop()
time.sleep(1)
backward()
time.sleep(3)
turnLeft()
time.sleep(3)