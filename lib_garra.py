from gpiozero import AngularServo
import time
import os



os.environ["PIGPIO_ADDR"] = "192.168.43.156"
os.environ["GPIOZERO_PIN_FACTORY"] = "pigpio"


def abrir_garra():

    srv = AngularServo(4,initial_angle = 0, min_angle=0, max_angle=90)
    srv.angle = 0    
    time.sleep(1)


def fechar_garra():

    srv = AngularServo(4,initial_angle = 0, min_angle= -90, max_angle=0)
    srv.angle = -3    
    time.sleep(1)
    
#abrir_garra()
#fechar_garra()
