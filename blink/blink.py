#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

while True:
    GPIO.output(14, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(14, GPIO.LOW)
    sleep(0.5)
