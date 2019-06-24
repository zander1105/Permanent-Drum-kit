#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LED1_PIN = 18

GPIO.setup(LED1_PIN, GPIO.OUT)

GPIO.output(LED1_PIN, False)
time.sleep(3)
GPIO.output(LED1_PIN, True)

GPIO.cleanup()
