from mcp3021_driver import MCP3021
import adc_plot
import time

voltage_values = []
time_values = []
duration = 3.0
dynamic_range = 5.23

try:
    adc = MCP3021(dynamic_range)

    time_start = time.time()

    while time.time() - time_start < duration:
        time_values += [time.time() - time_start]
        voltage_values += [adc.get_voltage()]

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()