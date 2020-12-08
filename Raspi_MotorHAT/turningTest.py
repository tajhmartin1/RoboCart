from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time, atexit

mh = Raspi_MotorHAT(addr=0x6f)

frontRight = mh.getMotor(1)
frontLeft = mh.getMotor(2)
backLeft = mh.getMotor(3)
backRight = mh.getMotor(4)

duration = 2
speed = 100

def forward():
    frontRight.run(Raspi_MotorHAT.FORWARD)
    frontLeft.run(Raspi_MotorHAT.FORWARD)
    backLeft.run(Raspi_MotorHAT.BACKWARD)
    backRight.run(Raspi_MotorHAT.BACKWARD)
    

def stop():
    frontRight.run(Raspi_MotorHAT.RELEASE)
    frontLeft.run(Raspi_MotorHAT.RELEASE)
    backLeft.run(Raspi_MotorHAT.RELEASE)
    backRight.run(Raspi_MotorHAT.RELEASE)

def turnRight():
    frontLeft.setSpeed(speed)
    backLeft.setSpeed(speed)
    forward()

def turnLeft():
    frontRight.setSpeed(speed)
    backRight.setSpeed(speed)
    forward()

def initialize():
    frontRight.setSpeed(100)
    frontLeft.setSpeed(100)
    backLeft.setSpeed(100)
    backRight.setSpeed(100)
    frontRight.run(Raspi_MotorHAT.FORWARD)
    frontLeft.run(Raspi_MotorHAT.FORWARD)
    backLeft.run(Raspi_MotorHAT.BACKWARD)
    backRight.run(Raspi_MotorHAT.BACKWARD)
    time.sleep(1)

turnLeft()
time.sleep(duration)
stop()


