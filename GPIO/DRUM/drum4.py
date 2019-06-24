#!/usr/bin/python
# coding: utf-8
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

BUTTON1_PIN = 19
LED1_PIN = 16
DRUM1_SOUND = "/root/GPIO/DRUM/sounds/drum3.mp3"

GPIO.setup(BUTTON1_PIN, GPIO.IN)
GPIO.setup(LED1_PIN, GPIO.OUT)

if GPIO.input(BUTTON1_PIN):
    print('Input was HIGH')
else:
    print('Input was LOW')

def DRUM1(BUTTON1_PIN):
	print ("Button Pressed!")
	if GPIO.input(BUTTON1_PIN):
    		print('Input was HIGH')
	else:
    		print('Input was LOW')

	GPIO.output(LED1_PIN, False)
	os.system('mpg321 -q ' + DRUM1_SOUND + ' &')
	time.sleep(0.05)
	GPIO.output(LED1_PIN, True)

print "Drum Module Test (CTRL+C to exit)"

time.sleep(2)

print "Ready"

try:
	GPIO.add_event_detect(BUTTON1_PIN, GPIO.FALLING, callback=DRUM1)

	while 1:
		time.sleep(100)

except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()

