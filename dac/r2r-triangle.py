from r2r_dac import R2R_DAC
import time

def tri(x):
    norm_x = x - x//4*4
    if norm_x < 2:
        return norm_x - 1
    else:
        return 4 - norm_x - 1

def get_triangle_amplitude(freq, t):
    return (tri(freq*t) + 1) / 2

def wait_for_sampling_period(sampling_freq):
    time.sleep(1/sampling_freq)

bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3
freq = 10
sampling_freq = 1000
amplitude = 3.2

if __name__ == "__main__":
    try:
        dac = R2R_DAC(bits, dynamic_range)

        while True:
            try:
                dac.set_voltage(amplitude * get_triangle_amplitude(freq, time.time()))
            except ValueError:
                print("Вы ввели не число. Попробуйте снова")
    except KeyboardInterrupt:
        print("До свидания!")
    finally:
        dac.deinit()