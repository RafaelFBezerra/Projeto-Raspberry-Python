from gpiozero import AngularServo
import time
import os



os.environ["PIGPIO_ADDR"] = "192.168.43.156"
os.environ["GPIOZERO_PIN_FACTORY"] = "pigpio"



def sentido_positivo():
    
    srv_base = AngularServo(2,initial_angle = 0, min_angle=0, max_angle=90)
    srv_base.min()
    srv_base.angle = 0    

    i=0.0
    while i<=90:
        srv_base.angle = i
        i = i + 1


def sentido_negativo():
    
    srv_base = AngularServo(2,initial_angle = 0, min_angle=-90, max_angle=0)
    srv_base.angle = 0    

    i=0.0
    while i>=-90:
        srv_base.angle = i
        i = i - 1


#sentido_positivo()
#sentido_negativo()
