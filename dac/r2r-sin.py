from r2r_dac import R2R_DAC
import numpy as np
import time

def get_sin_wave_amplitude(freq, t):
    return (np.sin(freq*t) + 1) / 2

def wait_for_sampling_period(sampling_freq):
    time.sleep(1/sampling_freq)

bits = [22, 27, 17, 26, 25, 21, 20, 16]
dynamic_range = 3.3
freq = 10
sampling_freq = 1000
amplitude = 3.2

if __name__ == "__main__":
    try:
        dac = R2R_DAC(bits, dynamic_range)

        while True:
            try:
                dac.set_voltage(amplitude * get_sin_wave_amplitude(freq, time.time()))
            except ValueError:
                print("Вы ввели не число. Попробуйте снова")
    except KeyboardInterrupt:
        print("До свидания!")
    finally:
        dac.deinit()