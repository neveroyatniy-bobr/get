from RPi import GPIO


dynamic_range = 3.3
def voltage_to_number(voltage):
    if (not(0 <= voltage <= dynamic_range)):
        print("Напряжение выходит за диапазон. Возрат 0.")
        return 0
    
    return int(voltage / dynamic_range * 255)

def dec2bin(dec):
    return [int(elem) for elem in bin(dec)[2:].zfill(8)]

def number_to_dac(num):
    bin_num = dec2bin(num)
    for i in range(len(bits)):
        GPIO.output(bits[i], bin_num[i])

GPIO.setmode(GPIO.BCM)

bits = [22, 27, 17, 26, 25, 21, 20, 16][::-1]

GPIO.setup(bits, GPIO.OUT)

try:
    while True:
        try:
            num = float(input("Введите напряжение в вольтах:"))
            number_to_dac(voltage_to_number(num))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова")
except KeyboardInterrupt:
        print("До свидания!")
finally:
    GPIO.output(bits, 0)
    GPIO.cleanup()