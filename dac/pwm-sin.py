from pwm_dac import PWM_DAC
import numpy as np
import time

def get_sin_wave_amplitude(freq, t):
    return (np.sin(freq*t) + 1) / 2

def wait_for_sampling_period(sampling_freq):
    time.sleep(1/sampling_freq)

dynamic_range = 3.3
freq = 10
sampling_freq = 60
amplitude = 3.2

gpio_pin = 12
pwm_frequency = 2000

if __name__ == "__main__":
    try:
        dac = PWM_DAC(gpio_pin, pwm_frequency, dynamic_range)

        while True:
            try:
                dac.set_voltage(amplitude * get_sin_wave_amplitude(freq, time.time()))
            except Exception:
                pass
    except KeyboardInterrupt:
        print("До свидания!")
    finally:
        dac.deinit()