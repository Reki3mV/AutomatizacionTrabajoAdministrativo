# -*- coding: utf-8 -*-
#!/usr/bin/python
#! Python
#import os

import re
import os.path as path
import subprocess
import errno
from getpass import getuser
import time
import pyautogui
import datetime

#COMANDO Pre USER/PASS!
userDeWindows = getuser()

#Tamaño de Pantalla
x,y = pyautogui.size()

################################################################################
#                           CARPETA DESKTOP
################################################################################

escritorio = str('C:\\Users\\' + userDeWindows + '\\Desktop\\')

################################################################################
#                           CARPETA BASE
################################################################################

Base = str(escritorio + 'Lazy' + userDeWindows + '\\')
try:
    os.mkdir(Base)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

################################################################################
#                           CARPETA """USER+PASS"""
################################################################################

Contraseña = str(Base + 'User+Pass'+'\\')
try:
    os.mkdir(Contraseña)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
    
################################################################################
#                      Levanta PASS previa SINO la Pide
################################################################################

def levantaPass():
    Contraseña = str(Base + 'User+Pass'+'\\')
    passSaTxt = str(Contraseña + userDeWindows + '-SaPass.txt')
    if path.exists(passSaTxt) == True:
        passRead = open(passSaTxt, 'r')
        largoPass = len(passRead.read())
        passRead.close()

        if largoPass >= 1:
            passRead = open(passSaTxt, 'r')
            global PASS
            PASS = passRead.read()
            passRead.close()

    else:
        print(" Ingrese Pass de SA")
        passSA = input(' ')
        passWrite = open(passSaTxt, 'w')
        passWrite.write(passSA)
        passWrite.close()
        
################################################################################
#                   Abriendo Sistema Administrativo
################################################################################

sa = str('c:\\SA\\sa.exe')
def abreSOSA():
    os.system('C:\SA\sa.exe')
    
    
def abriendoSA():
    pyautogui.hotkey('win', 'r')                        #Ejecuta Win+R
    time.sleep(1)
    pyautogui.typewrite(sa, interval=0.1)               #Escribe Dir SA
    pyautogui.hotkey('enter',interval=1)                #Enter
    time.sleep(1)
    pyautogui.hotkey('tab')                             #TAB
    pyautogui.typewrite(PASS, interval=0.5)             #Escribe PASS
    pyautogui.hotkey('enter',interval=1)                #Enter
    time.sleep(3)

############################################################################
#                       ENVIO DE NOTAS // CONEXIONES, DATOS, RECLAMOS.
############################################################################

def envioDeNotas():

            #################################################
            #Envio de Conexiones
            #Menu Desplegable
            pyautogui.moveTo(1247, 154, duration=0.5)
            pyautogui.click(1247, 154)
            
            #Selecciona Intervenciones
            pyautogui.moveTo(1240, 172, duration=0.5)
            pyautogui.click(1240, 172)
            time.sleep(0.5)

            #Seleccionar TODO
            pyautogui.moveTo(1206, 225, duration=0.5)
            pyautogui.click(1206, 225)
            time.sleep(0.5)

            #Enviar Notas
            pyautogui.moveTo(1203, 330, duration=0.5)
            pyautogui.click(1203, 330)

            #Trae al Frente la BOX
            time.sleep(3)
            pyautogui.click(1203, 330)
            
            #ACEPTAR "Se realizaron los Envios Automaticamente"
            pyautogui.hotkey('enter', interval=1)

            #################################################
            #Envio de Datos
            #Menu Desplegable
            pyautogui.moveTo(1247, 154, duration=0.5)
            pyautogui.click(1247, 154)
            
            #Seleccion de Info de Datos
            pyautogui.moveTo(1226, 187, duration=0.5)
            pyautogui.click(1226, 187)
            
            #Seleccionar TODO
            pyautogui.moveTo(1206, 225, duration=0.5)
            pyautogui.click(1206, 225)
            time.sleep(0.5)
            
            #Enviar Notas
            pyautogui.moveTo(1203, 330, duration=0.5)
            pyautogui.click(1203, 330)

            #Trae al Frente la BOX
            time.sleep(3)
            pyautogui.click(1203, 330)
            
            #ACEPTAR "Se realizaron los Envios Automaticamente"
            pyautogui.hotkey('enter', interval=1)

            #################################################
            #Envio de Reclamos
            #Menu Desplegable
            pyautogui.moveTo(1247, 154, duration=0.5)
            pyautogui.click(1247, 154)
            
            #Seleccion de Reclamos
            pyautogui.moveTo(1216, 198, duration=0.5)
            pyautogui.click(1216, 198)
            
            #Seleccionar TODO
            pyautogui.moveTo(1206, 225, duration=0.5)
            pyautogui.click(1206, 225)
            time.sleep(0.5)
            
            #Enviar Notas
            pyautogui.moveTo(1203, 330, duration=0.5)
            pyautogui.click(1203, 330)

            #Trae al Frente la BOX
            time.sleep(3)
            pyautogui.click(1203, 330)
            
            #ACEPTAR "Se realizaron los Envios Automaticamente"
            pyautogui.hotkey('enter', interval=1)

            time.sleep(1)

def opciones():    
    print("\n"+ "\n"+ "\n"+ "\n"+ "\n")
    print('                       LazyGv ')
    print('                       ══════'+ "\n")
    input(' Press ENTER to Continue...'+'\n')
    
    #################################################
    #Abriendo Sistema Administrativo SA
    #################################################

    abriendoSA()
    
    #################################################
    #Gestion de Conexiones
    #################################################

    pyautogui.moveTo(73, 35, duration=0.5)
    pyautogui.click(73, 35)
    
    #################################################
    #Adelantos firmados
    #################################################

    pyautogui.moveTo(100, 55, duration=0.5)
    pyautogui.click(100, 55)

    time.sleep(1)
    
    while True:
        envioDeNotas()


################################################################################

levantaPass()
opciones()
