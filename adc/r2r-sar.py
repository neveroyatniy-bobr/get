from r2r_adc import R2R_ADC
import adc_plot
import time

voltage_values = []
time_values = []
duration = 3.0
dynamic_range = 3.3

try:
    adc = R2R_ADC(dynamic_range, compare_time=0.007)

    time_start = time.time()

    while time.time() - time_start < duration:
        time_values += [time.time() - time_start]
        voltage_values += [adc.get_sar_voltage()]

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()