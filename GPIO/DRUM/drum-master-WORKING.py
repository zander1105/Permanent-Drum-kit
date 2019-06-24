#!/usr/bin/python
# coding: utf-8
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

BUTTON1_PIN = 17
LED1_PIN = 18
DRUM1_SOUND = "/root/GPIO/DRUM/sounds/drum1.mp3"

BUTTON2_PIN = 22
LED2_PIN = 23
DRUM2_SOUND = "/root/GPIO/DRUM/sounds/drum2.mp3"

BUTTON3_PIN = 6 
LED3_PIN = 12 
DRUM3_SOUND = "/root/GPIO/DRUM/sounds/drum3.mp3"

BUTTON4_PIN = 19
LED4_PIN = 16
DRUM4_SOUND = "/root/GPIO/DRUM/sounds/drum4.mp3"

################## Put GPIO.setup Button / Toggle 5 in here #####################

#BUTTON5_PIN = ??
#LED4_PIN = ??

##################################################################################

GPIO.setup(BUTTON1_PIN, GPIO.IN)
GPIO.setup(LED1_PIN, GPIO.OUT)

GPIO.setup(BUTTON2_PIN, GPIO.IN)
GPIO.setup(LED2_PIN, GPIO.OUT)

GPIO.setup(BUTTON3_PIN, GPIO.IN)
GPIO.setup(LED3_PIN, GPIO.OUT)

GPIO.setup(BUTTON4_PIN, GPIO.IN)
GPIO.setup(LED4_PIN, GPIO.OUT)

################## Put GPIO.setup Button / Toggle 5 in here #####################


#################################################################################

#if GPIO.input(BUTTON1_PIN):
#    print('Input was HIGH')
#else:
#    print('Input was LOW')

def DRUM1(BUTTON1_PIN):
	print ("Button 1 Pressed!")
	if GPIO.input(BUTTON1_PIN):
    		print('Input was HIGH')
	else:
    		print('Input was LOW')
		GPIO.output(LED1_PIN, False)
		os.system('mpg321 -q ' + DRUM1_SOUND + ' &')
		time.sleep(0.5)
		GPIO.output(LED1_PIN, True)

def DRUM2(BUTTON2_PIN):
	print ("Button 2 Pressed!")
	if GPIO.input(BUTTON2_PIN):
    		print('Input was HIGH')
	else:
    		print('Input was LOW')
		GPIO.output(LED2_PIN, False)
		os.system('mpg321 -q ' + DRUM2_SOUND + ' &')
		time.sleep(0.05)
		GPIO.output(LED2_PIN, True)

def DRUM3(BUTTON3_PIN):
	print ("Button 3 Pressed!")
	if GPIO.input(BUTTON3_PIN):
    		print('Input was HIGH')
	else:
    		print('Input was LOW')

	GPIO.output(LED3_PIN, False)
	os.system('mpg321 -q ' + DRUM3_SOUND + ' &')
	time.sleep(0.05)
	GPIO.output(LED3_PIN, True)

def DRUM4(BUTTON4_PIN):
	print ("Button 4 Pressed!")
	if GPIO.input(BUTTON4_PIN):
    		print('Input was HIGH')
	else:
    		print('Input was LOW')

	GPIO.output(LED4_PIN, False)
	os.system('mpg321 -q ' + DRUM4_SOUND + ' &')
	time.sleep(0.05)
	GPIO.output(LED4_PIN, True)

################## Put Button / Toggle 5 main code in here #####################


#################################################################################


print "Drum Module Test (CTRL+C to exit)"

time.sleep(2)

GPIO.output(LED1_PIN, False)
time.sleep(0.2)
GPIO.output(LED2_PIN, False)
time.sleep(0.2)
GPIO.output(LED3_PIN, False)
time.sleep(0.2)
GPIO.output(LED4_PIN, False)
time.sleep(0.5)

################## Put GPIO.output LED 5 in here #####################


#################################################################################


GPIO.output(LED4_PIN, True)
time.sleep(0.2)
GPIO.output(LED3_PIN, True)
time.sleep(0.2)
GPIO.output(LED2_PIN, True)
time.sleep(0.2)
GPIO.output(LED1_PIN, True)
time.sleep(0.5)

################## Put GPIO.output LED 5 in here #####################


#################################################################################


print "Ready"

try:
	GPIO.add_event_detect(BUTTON1_PIN, GPIO.FALLING, callback=DRUM1)
	GPIO.add_event_detect(BUTTON2_PIN, GPIO.FALLING, callback=DRUM2)
	GPIO.add_event_detect(BUTTON3_PIN, GPIO.FALLING, callback=DRUM3)
	GPIO.add_event_detect(BUTTON4_PIN, GPIO.FALLING, callback=DRUM4)

################## Put GPIO Event handling butoon 5 in here #####################


#################################################################################


	while 1:
		time.sleep(100)

except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()

