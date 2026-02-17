from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
light = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(light, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(light))
    time.sleep(0.1)