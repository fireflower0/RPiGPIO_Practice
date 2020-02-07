#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import RPi.GPIO as GPIO
from time import sleep

redPin   = 17
bluePin  = 22
greenPin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,   GPIO.OUT)
GPIO.setup(bluePin,  GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

while True:
    GPIO.output(redPin,   False)
    GPIO.output(bluePin,  False)
    GPIO.output(greenPin, False)
    sleep(0.5)
    GPIO.output(redPin,   True)
    GPIO.output(bluePin,  False)
    GPIO.output(greenPin, False)
    sleep(0.5)
    GPIO.output(redPin,   False)
    GPIO.output(bluePin,  True)
    GPIO.output(greenPin, False)
    sleep(0.5)
    GPIO.output(redPin,   False)
    GPIO.output(bluePin,  False)
    GPIO.output(greenPin, True)
    sleep(0.5)
    GPIO.output(redPin,   True)
    GPIO.output(bluePin,  True)
    GPIO.output(greenPin, True)
    sleep(0.5)
