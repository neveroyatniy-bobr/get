from mcp4725 import MCP4725
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

dynamic_range = 5
freq = 10
sampling_freq = 500
amplitude = 3.2

if __name__ == "__main__":
    try:
        dac = MCP4725(dynamic_range, verbose=False)

        while True:
            try:
                dac.set_voltage(amplitude * get_triangle_amplitude(freq, time.time()))
            except Exception:
                pass
    except KeyboardInterrupt:
        print("До свидания!")
    finally:
        dac.deinit()