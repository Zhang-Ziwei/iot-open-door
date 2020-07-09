#!/usr/bin/env python3
# coding:UTF-8
"""
servo_test.py
www.bluetin.io
16/01/2018
"""
import requests
import re
__author__ = "Mark Heywood"
__version__ = "0.01"
__license__ = "MIT"

import uuid
# import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep

# Adjust the pulse values to set rotation range
min_pulse = 0.000544    # Library default = 1/1000
max_pulse = 0.0024      # Library default = 2/1000
# Initial servo position
pos = 0
test = 0

servo = Servo(2, pos, min_pulse, max_pulse, 40/1000, None)

############
#LED_PIN = 2
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED_PIN, GPIO.OUT)
data = 'off'
#define=0
try:
    #print('')
    while True:
        try:
            while True:
                fil=requests.get('http://ziyan.azurewebsites.net/thuiotproject/stat.txt')
                print("#####")
                print(fil.text)
                #if(re.search("content=\'1",fil.text)):
                    #define=1
                #elif(re.search("content=\'0",fil.text)):
                    #define=0
                #elif(re.search("content=\'2",fil.text)):
                    #define=2
                #########
                #print(define)
                if(fil.text=='1'):
                    data = 'on'
                elif(fil.text=='0'):
                    data = 'off'
                else:
                    data='stop'
                #########
                if data == 'on':
                    print(data)
                    servo.value = 1
                    print('開燈')
                    data='stop'
                    fil2=requests.get('http://ziyan.azurewebsites.net/thuiotproject/ask.php?chstat=a')
                elif data == 'off':
                    #GPIO.output(LED_PIN, GPIO.LOW)
                    servo.value =0.2
                    data='stop'
                    #for pos in range(20, -1, -1):               
                        # pos = pos * 0.1 + 1
                        #servo.value = pos
                        #print(pos)
                        #sleep(0.05)
                    print('關燈')
                    fil3=requests.get('http://ziyan.azurewebsites.net/thuiotproject/ask.php?chstat=a')
                else:
                    print('未知的指令: {}'.format(data))
        except IOError:
            pass
        client_socket.close()
        print('中斷連線')


except KeyboardInterrupt:
    print('中斷程式')
finally:
    #GPIO.cleanup()
    print('中斷連線')
####

####