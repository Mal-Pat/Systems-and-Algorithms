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

void insertionSort(int a[], int size)
{
    for (int i = 1; i < size; ++i) {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j = j - 1;
        }
        a[j + 1] = key;
    }
}

void mergeArrays(int a[], int left, int mid, int right) {
    int len1 = mid - left + 1;
    int len2 = right - mid;

    int L[len1], R[len2];

    for (int i = 0; i < len1; i++)
        L[i] = a[left + i];
    for (int j = 0; j < len2; j++)
        R[j] = a[mid + 1 + j];

    int i = 0, j = 0;
    int k = left;

    while (i < len1 && j < len2) {
        if (L[i] <= R[j]) {
            a[k] = L[i];
            i++;
        } else {
            a[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < len1) {
        a[k] = L[i];
        k++;
        i++;
    }

    while (j < len2) {
        a[k] = R[j];
        k++;
        j++;
    }
}

void mergeSort(int a[], int left, int right) {
    if (left >= right)
        return;

    int mid = left + (right - left) / 2;
    mergeSort(a, left, mid);
    mergeSort(a, mid + 1, right);
    mergeArrays(a, left, mid, right);
}

void printArray(int A[], int size) {
    cout << "[";
    for (int i = 0; i < size; i++) {
        cout << A[i];
        if (!(i==size-1)) {
            cout << ", ";
        }
    }
    cout << "]\n";
}

void randomInputArray(int A[], int size) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distr(1, 1000000);

    for (int i = 0; i < size; i++) {
        A[i] = distr(gen);
    }
}

/*
int main() {
    int arr[10];
    randomInputArray(arr,10);
    printArray(arr, 10);
    insertionSort(arr, 10);
    printArray(arr, 10);
}
*/

int main() {
    ofstream outfile("Data/mergeSort_analysis-1_5-10000-5_5.txt");
    if (outfile.is_open()) {
        for (int i = 5; i <= 10000; i = i + 5) {
            float avg_time = 0;
            int arr[i];
            for (int j = 0; j < 5; j++) {
                randomInputArray(arr, i);
                auto start = high_resolution_clock::now();
                mergeSort(arr, 0, i - 1);
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
