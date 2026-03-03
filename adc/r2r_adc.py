from RPi import GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = True):
        self.dynamic_range = dynamic_range
        self.compare_time = compare_time
        self.verbose = verbose

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def dec2bin(self, dec):
        return [int(elem) for elem in bin(dec)[2:].zfill(8)]

    def number_to_dac(self, num):
        bin_num = self.dec2bin(num)
        for i in range(len(self.bits_gpio)):
            GPIO.output(self.bits_gpio[i], bin_num[i])
    
    def sequal_counting_adc(self):
        for num in range(256):
            self.number_to_dac(num)
            time.sleep(self.compare_time)

            is_above = GPIO.input(self.comp_gpio)
            if is_above:
                return num
        
        return 255
    
    def get_sc_voltage(self):
        return self.sequal_counting_adc() / 255 * self.dynamic_range

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.3)

        while True:
            print(f"Напряжение на аналоговом входе: {adc.get_sc_voltage()} В")

    except KeyboardInterrupt:
        print("")
        print("До свидания!")           
        
    finally:
        adc.deinit()