#include <iostream>
#include <chrono>
#include <random>
#include <fstream>
#include <string>

using namespace std;
using namespace std::chrono;

int getMin(int a[], int i, int j) {
    int min = i;
    for(int k = i + 1; k <= j; k++) {
        if (a[k] < a[min]) {
            min = k;
        }
    }
    return min;
}

void selectionSort(int a[], int size) {
    for (int i = 0; i < size; i++) {
        int min = getMin(a, i, size - 1);
        int t = a[min];
        a[min] = a[i];
        a[i] = t;
    }
}

void randomInputArray(int A[], int size) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distr(1, 1000000);

    for (int i = 0; i < size; i++) {
        A[i] = distr(gen);
    }
}

int main() {
    ofstream outfile("selection_analysis_5_10000_5.txt");
    if (outfile.is_open()) {
        for (int i = 5; i <= 10000; i = i + 5) {
            float avg_time = 0;
            int arr[i];
            for (int j = 0; j < 5; j++) {
                randomInputArray(arr, i);
                auto start = high_resolution_clock::now();
                selectionSort(arr, i);
                auto stop = high_resolution_clock::now();
                auto duration = duration_cast<microseconds>(stop - start);
                avg_time = avg_time + duration.count();
            }
            outfile << i << endl;
            outfile << avg_time/5 << endl;
        }
        outfile.close();
    } else {
        cout << "Error opening file for writing." << endl;
    }
    return 0;
}
