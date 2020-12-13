from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time

#import atextit;

mh = Raspi_MotorHAT(addr=0x6f)


m1 = mh.getMotor(1)
m2 = mh.getMotor(2)
m3 = mh.getMotor(3)
m4 = mh.getMotor(4)

m1.setSpeed()
# def stop():
# 	m2.run(Raspi_MotorHAT.RELEASE)
#     m1.run(Raspi_MotorHAT.RELEASE)

# m2.setSpeed(150)
# m1.setSpeed(150)

# for i in range (0, 100):
#     m2.run(Raspi_MotorHAT.FORWARD)
#     m1.run(Raspi_MotorHAT.FORWARD)

x = 0

#while x < 510:
  #  m2.setSpeed(x/2)
    #m1.setSpeed(x/2)
    #m2.run(Raspi_MotorHAT.FORWARD)
    #m1.run(Raspi_MotorHAT.FORWARD)
   # x += 1

#while x > 50:
   # m2.setSpeed(x/2)
    #m1.setSpeed(x/2)
    #m2.run(Raspi_MotorHAT.FORWARD)
    #m1.run(Raspi_MotorHAT.FORWARD)
    #x -= 1
while x < 10 :




m2.run(Raspi_MotorHAT.RELEASE)
m1.run(Raspi_MotorHAT.RELEASE)

