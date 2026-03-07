import matplotlib.pyplot as plt

def plot_voltage_vs_time(times, voltage, max_voltage):
    plt.figure(figsize = (10, 6))
    plt.plot(times, voltage)
    plt.title("График напряжения от времени")
    plt.xlabel("Время t, с")
    plt.ylabel("Напряжение V, В")
    plt.xlim(0)
    plt.ylim(0, max_voltage+1)
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(times):
    sampling_periods = []
    for i in range(len(times) - 1):
        sampling_periods.append(times[i+1] - times[i])

    plt.figure(figsize = (10, 6))
    plt.hist(sampling_periods)
    plt.title("Гситограмма периодов измерений")
    plt.xlabel("Периоды dt, с")
    plt.ylabel("Количество измерений n, шт")
    plt.xlim(0, 0.06)
    plt.ylim(0)
    plt.grid(True)
    plt.show()