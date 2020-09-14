from gpiozero import Motor
import os
import sys
import time

os.environ["PIGPIO_ADDR"] = "192.168.43.156"
os.environ["GPIOZERO_PIN_FACTORY"] = "pigpio"
motor = Motor(26,20)

def esteira_positivo():

    for i in range (1,13):
        time.sleep(1)
        motor.forward(speed = 1)
    motor.stop()

def esteira_negativo():
    for i in range (1,13):
        time.sleep(1)
        motor.backward(speed = 1)
    motor.stop()
    
#esteira_positivo()
esteira_negativo()


#motor.stop()
   
