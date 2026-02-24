from mcp4725 import MCP4725
import numpy as np
import time

def get_sin_wave_amplitude(freq, t):
    return (np.sin(freq*t) + 1) / 2

def wait_for_sampling_period(sampling_freq):
    time.sleep(1/sampling_freq)

dynamic_range = 5
freq = 10
sampling_freq = 60
amplitude = 3.2

if __name__ == "__main__":
    try:
        dac = MCP4725(dynamic_range, verbose=False)

        while True:
            try:
                dac.set_voltage(amplitude * get_sin_wave_amplitude(freq, time.time()))
            except Exception:
                pass
    except KeyboardInterrupt:
        print("До свидания!")
    finally:
        dac.deinit()