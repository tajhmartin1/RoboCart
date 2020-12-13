from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time

mh = Raspi_MotorHAT(addr=0x6f);


m1 = mh.getMotor(1);

m1.setSpeed(150);
m1.run(Raspi_MotorHAT.FORWARD)
time.sleep(3)
m1.run(Raspi_MotorHAT.RELEASE)
