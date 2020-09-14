import lib_servo
import lib_voz
import lib_motor
import lib_garra
import os
import time
import sys


lib_garra.abrir_garra()
time.sleep(2)
lib_garra.fechar_garra()
time.sleep(2)
lib_servo.sentido_positivo()
time.sleep(2)
lib_garra.abrir_garra()
time.sleep(2)
lib_voz.voz_deixa_obj()
lib_motor.esteira_positivo()
lib_voz.voz_ret_obj()
time.sleep(5)
lib_voz.voz_ret_est()
lib_motor.esteira_negativo()
lib_voz.voz_ret_braco()
lib_servo.sentido_negativo()

