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

pushed = [0, 0]

while True:
    if not(GPIO.input(sub_button)) and not(GPIO.input(add_button)):
        if (pushed[0] and pushed[1]):
            cnt = 2**leds_cnt-1
            binary_cnt = list(map(int, bin(cnt)[2:].zfill(8)))
            for i in range(leds_cnt):
                GPIO.output(leds[i], binary_cnt[i])
            time.sleep(0.2)
            pushed = [0, 0]
            continue

        if pushed[0]:
            cnt = (cnt + 1) % (2**leds_cnt)
            binary_cnt = list(map(int, bin(cnt)[2:].zfill(8)))
            for i in range(leds_cnt):
                GPIO.output(leds[i], binary_cnt[i])
            time.sleep(0.2)
            pushed = [0, 0]
            continue

        if pushed[1]:
            cnt = (cnt - 1) % (2**leds_cnt)
            binary_cnt = list(map(int, bin(cnt)[2:].zfill(8)))
            for i in range(leds_cnt):
                GPIO.output(leds[i], binary_cnt[i])
            time.sleep(0.2)
            pushed = [0, 0]
            continue

    if GPIO.input(add_button):
        pushed[0] = 1

    if GPIO.input(sub_button):
        pushed[1] = 1