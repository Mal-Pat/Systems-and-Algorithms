# Time and Length Analysis

Finding the maximum length of a array that can be sorted under 5 minutes using various sorting algorithms on a particular computer system.

The array is randomly generated with integer values following a `Uniform(1,1000000)` distribution.

Since time is taken in milliseconds, `5 min = 300 s = 300000 ms`

## Selection Sort

Time complexity = `O(n^2)`

Trendline Equation = `0.000402*(n^2) + 0.088*n - 2.87`

Solving `300000 = 0.000402*(n^2) + 0.088*n - 2.87`,

We get `n = 27208` approximately.

**Therefore, `max n = 27,208`**

## Insertion Sort

Time complexity = `O(n^2)`

Trendline Equation = `0.000261*(n^2) + 0.0358*n - 25.67`

Solving `300000 = 0.000261*(n^2) + 0.0358*n - 25.67`,

We get `n = 33836` approximately.

**Therefore, `max n = 33,836`**

## Merge Sort

Time complexity = `O(n*log2(n))`

Trendline Equation = `0.00752*(n*log2(n)) - 0.000828*n + 8.93`

Solving `300000 = 0.00752*(n*log2(n)) - 0.000828*n + 8.93`,

We get `n = 1921274` approximately.

**Therefore, `max n = 1,921,274`**