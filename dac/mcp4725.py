import smbus

class MCP4725:
    def __init__(self, dynamic_range, address = 0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range
    
    def deinit(self):
        self.bus.close()
    
    def set_number(self, number):
        if not isinstance(number, int):
            print("На вхожд ЦАП можно только целое число")
        
        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4725(12 бит)")
        
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(self.address, first_byte, second_byte)

        if self.verbose:
            print(f"Число {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]")

    def voltage_to_number(self, voltage):
        if (not(0 <= voltage <= self.dynamic_range)):
            print("Напряжение выходит за диапазон. Возрат 0.")
            return 0
        
        return int(voltage / self.dynamic_range * 4095)

    def set_voltage(self, voltage):
        self.set_number(self.voltage_to_number(voltage))

dynamic_range = 5.0

if __name__ == "__main__":
    try:
        dac = MCP4725(dynamic_range)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах:"))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте снова")
    except KeyboardInterrupt:
        print()
        print("До свидания!")
    finally:
        dac.deinit()