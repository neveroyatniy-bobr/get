from RPi import GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        self.pwm.stop()
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        duty = voltage / self.dynamic_range * 100
        self.pwm.ChangeDutyCycle(duty)

gpio_pin = 12
pwm_frequency = 200
dynamic_range = 3.3

if __name__ == "__main__":
    try:
        dac = PWM_DAC(gpio_pin, pwm_frequency, dynamic_range)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах:"))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте снова")
    except KeyboardInterrupt:
        print("")
        print("До свидания!")
    finally:
        dac.deinit()