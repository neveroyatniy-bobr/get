from RPi import GPIO

class R2R_DAC:
    def __init__(self, bits, dynamic_range):
        self.bits = bits[::-1]
        self.dynamic_range = dynamic_range

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits, GPIO.OUT, initial = 0)
    
    def dec2bin(self, dec):
        return [int(elem) for elem in bin(dec)[2:].zfill(8)]

    def voltage_to_number(self, voltage):
        if (not(0 <= voltage <= self.dynamic_range)):
            print("Напряжение выходит за диапазон. Возрат 0.")
            return 0
        
        return int(voltage / self.dynamic_range * 255)
    
    def number_to_dac(self, num):
        bin_num = self.dec2bin(num)
        for i in range(len(self.bits)):
            GPIO.output(self.bits[i], bin_num[i])
    
    def set_voltage(self, voltage):
        self.number_to_dac(self.voltage_to_number(voltage))

    def deinit(self):
        GPIO.output(self.bits, 0)
        GPIO.cleanup()

bits = [22, 27, 17, 26, 25, 21, 20, 16]
dynamic_range = 3.3

if __name__ == "__main__":
    try:
        dac = R2R_DAC(bits, dynamic_range)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах:"))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте снова")
    except KeyboardInterrupt:
        print("До свидания!")
    finally:
        dac.deinit()