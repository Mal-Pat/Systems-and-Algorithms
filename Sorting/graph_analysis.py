import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as optimize

def selection_sort_graph():
    lengths = []
    times = []

    with open("Data/selectionSort_analysis-1_5-10000-5_5.txt", "r") as infile:
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

    plt.plot(lengths, times, color="red", label="Data")

    coeffs = np.polyfit(lengths, times, 2)
    print(coeffs)

    fit_func = np.poly1d(coeffs)
    plt.plot(lengths, fit_func(lengths), color="blue", label="Trendline")

    plt.text(2000, 30000, f"{round(coeffs[0],6)}*(n^2) + {round(coeffs[1],4)}*n + ({round(coeffs[2],2)})")

    plt.xlabel("Length n")
    plt.ylabel("Time (ms)")
    plt.title("Selection Sort - Length vs Time")
    plt.legend()

    plt.savefig('Graphs/selectionSort_analysis-1_5-10000-5_5.png')

def insertion_sort_graph():
    lengths = []
    times = []

    with open("Data/insertionSort_analysis-1_5-10000-5_5.txt", "r") as infile:
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

    plt.plot(lengths, times, color="red", label="Data")

    coeffs = np.polyfit(lengths, times, 2)
    print(coeffs)

    fit_func = np.poly1d(coeffs)
    plt.plot(lengths, fit_func(lengths), color="blue", label="Trendline")

    plt.text(1500, 18000, f"{round(coeffs[0],6)}*(n^2) + {round(coeffs[1],4)}*n + ({round(coeffs[2],2)})")

    plt.xlabel("Length n")
    plt.ylabel("Time (ms)")
    plt.title("Insertion Sort - Length vs Time")
    plt.legend()

    plt.savefig('Graphs/insertionSort_analysis-1_5-10000-5_5.txt.png')

def nlogn(x, a, b, c):
    return (a * x * np.log2(x)) + (b * x) + c

def merge_sort_graph():
    lengths = []
    times = []

    with open("Data/mergeSort_analysis-1_5-10000-5_5.txt", "r") as infile:
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

    lengths, times = np.array(lengths), np.array(times)

    plt.plot(lengths, times, color="red", label="Data")

    popt, pcov = optimize.curve_fit(nlogn, lengths, times)
    print(popt)

    plt.plot(lengths, nlogn(lengths, *popt), color="blue", label="Trendline")

    plt.text(2500, 120, f"{round(popt[0],5)}*(n*log2(n)) + ({round(popt[1],6)})*n + {round(popt[2],2)}")

    plt.xlabel("Length n")
    plt.ylabel("Time (ms)")
    plt.title("Merge Sort - Length vs Time")
    plt.legend()

    plt.savefig('Graphs/mergeSort_analysis-1_5-10000-5_5.txt.png')

def plot_three_sorts():
    lengths = []
    times_sel = []
    times_ins = []
    times_mer = []

    with open("Data/selectionSort_analysis-1_5-10000-5_5.txt", "r") as infile:
        state = 0
        for line in infile:
            if state == 0:
                lengths.append(int(line))
                state = 1
            elif state == 1:
                times_sel.append(float(line))
                state = 0
            else:
                print('what even happened?')

    with open("Data/insertionSort_analysis-1_5-10000-5_5.txt", "r") as infile:
        state = 0
        for line in infile:
            if state == 0:
                state = 1
            elif state == 1:
                times_ins.append(float(line))
                state = 0
            else:
                print('what even happened?')

    with open("Data/mergeSort_analysis-1_5-10000-5_5.txt", "r") as infile:
        state = 0
        for line in infile:
            if state == 0:
                state = 1
            elif state == 1:
                times_mer.append(float(line))
                state = 0
            else:
                print('what even happened?')

    plt.plot(lengths, times_sel, color="blue", label="Selection Sort")
    plt.plot(lengths, times_ins, color="green", label="Inserion Sort")
    plt.plot(lengths, times_mer, color="red", label="Merge Sort")


    plt.xlabel("Length n")
    plt.ylabel("Time (ms)")
    plt.title("Three Sorts - Length vs Time")
    plt.legend()

    plt.savefig('Graphs/threeSorts_analysis-1_5-10000-5_5.txt.png')
