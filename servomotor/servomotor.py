import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

gpio_out = 24
GPIO.setup(gpio_out, GPIO.OUT)

servo = GPIO.PWM(gpio_out, 50)

servo.start(0)

for i in range(3):
    servo.ChangeDutyCycle(2.5)
    sleep(0.5)
    servo.ChangeDutyCycle(7.25)
    sleep(0.5)
    servo.ChangeDutyCycle(12)
    sleep(0.5)
    servo.ChangeDutyCycle(7.25)
    sleep(0.5)

servo.stop()
GPIO.cleanup()
