#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)
print ("1")
GPIO.setup(12, GPIO.OUT)
print("2")

while True:
     if GPIO.input(23):
         GPIO.output(12, True)
     else:
         GPIO.output(12, False)
