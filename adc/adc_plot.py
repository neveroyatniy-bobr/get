import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize = (10, 6))
    plt.plot(time, voltage)
    plt.title("График напряжения от времени")
    plt.xlabel("Время t, с")
    plt.ylabel("Напряжение V, В")
    plt.xlim(0)
    plt.ylim(0, max_voltage+1)
    plt.grid(True)
    plt.show()