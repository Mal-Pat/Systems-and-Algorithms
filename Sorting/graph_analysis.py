import numpy as np 
import matplotlib.pyplot as plt

def selection_sort_graph():
    lengths = []
    times = []

    with open("selection_analysis_5_10000_5.txt", "r") as infile:
        state = 0
        for line in infile:
            if state == 0:
                lengths.append(int(line))
                state = 1
            elif state == 1:
                times.append(float(line))
                state = 0
            else:
                print('what even happened?')

    plt.plot(lengths, times, color="red")

    coeffs = np.polyfit(lengths, times, 2)
    print(coeffs)

    fit_func = np.poly1d(coeffs)
    plt.plot(lengths, fit_func(lengths), color="blue")

    plt.text(2000, 30000, f"{round(coeffs[0],6)}*(x^2) + {round(coeffs[1],4)}*x + ({round(coeffs[2],2)})")

    plt.xlabel("Length n")
    plt.ylabel("Time (ms)")
    plt.title("Selection Sort - Length vs Time")

    plt.savefig('selection_analysis_5_10000_5.png')

selection_sort_graph()