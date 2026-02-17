from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
leds_cnt = len(leds)
GPIO.setup(leds, GPIO.OUT)

add_button = 9
GPIO.setup(add_button, GPIO.IN)

sub_button = 10
GPIO.setup(sub_button, GPIO.IN)

GPIO.output(leds, 0)

cnt = 0

while True:
    if GPIO.input(add_button):
        cnt = (cnt + 1) % (2**leds_cnt)
        binary_cnt = list(map(int, bin(cnt)[2:].zfill(8)))
        for i in range(leds_cnt):
            GPIO.output(leds[i], binary_cnt[i])
        time.sleep(0.2)

    if GPIO.input(sub_button):
        cnt = (cnt - 1) % (2**leds_cnt)
        binary_cnt = list(map(int, bin(cnt)[2:].zfill(8)))
        for i in range(leds_cnt):
            GPIO.output(leds[i], binary_cnt[i])
        time.sleep(0.2)

        