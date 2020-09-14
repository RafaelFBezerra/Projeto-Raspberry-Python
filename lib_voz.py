import pyttsx3
import time


def voz_verif_obj():
    voz_init = pyttsx3.init('sapi5')
    voz_init.say('OBJETO DETECTADO!')
    voz_init.runAndWait()
def voz_deixa_obj():
    voz_init = pyttsx3.init('sapi5')
    voz_init.say('ACIONANDO A ESTEIRA!')
    voz_init.runAndWait()
def voz_ret_obj():
    voz_init = pyttsx3.init('sapi5')
    voz_init.say('RETIRE O OBJETO EM ATÉ 5 SEGUNDOS!')
    voz_init.runAndWait()
def voz_ret_est():
    voz_init = pyttsx3.init('sapi5')
    voz_init.say('RETORNANDO A ESTEIRA A POSIÇÃO INICIAL!')
    voz_init.runAndWait()
def voz_ret_braco():
    voz_init = pyttsx3.init('sapi5')
    voz_init.say('RETORNANDO O BRAÇO A POSIÇÃO INICIAL!')
    voz_init.runAndWait()
