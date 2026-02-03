# Sorting Algorithm Stress Test (Prelim Exam)

## Project Overview

This benchmarking tool analyzes the efficiency of fundamental sorting algorithms when handling structured data at scale. The application processes a dataset of **100,000 records** (ID, FirstName, LastName) and measures performance across different data sizes (**1,000**, **10,000**, and **100,000** rows) and data types.

## Laboratory Objectives

- **From-Scratch Implementation**: Manual implementation of Bubble Sort, Insertion Sort, and Merge Sort without built-in libraries.
- **Scalability Testing**: Benchmarking algorithms at 1k, 10k, and 100k records.
- **Structured Data Handling**: Sorting objects based on Integer (ID) and String (Name) comparisons.
- **Performance Analysis**: Measuring the impact of **O(n²)** vs **O(n log n)** time complexity.

---

## Benchmark Results

The following table summarizes execution time for sorting by **ID**.  
*Note: O(n²) algorithms are often too slow to complete 100,000 rows within a reasonable timeframe.*

| Algorithm        | 1,000 Rows | 10,000 Rows | 100,000 Rows |
|------------------|------------|-------------|--------------|
| *Bubble Sort*    | ~0.04s     | ~4.15s      | >10 min (DNF) |
| *Insertion Sort* | ~0.01s     | ~1.12s      | >5 min (DNF) |
| *Merge Sort*     | ~0.003s    | ~0.03s      | ~0.35s       |

---

## Technical Analysis

- **The O(n log n) Standard**: Merge Sort demonstrated consistent efficiency regardless of data size. While it requires additional memory (O(n) space), its speed makes it the standard for large-scale computing.
- **The O(n²) Bottleneck**: Bubble Sort and Insertion Sort showed exponential time growth. A **10×** increase in data size resulted in approximately a **100×** increase in execution time, making them impractical for large datasets.

---

## Repository Structure

```text
/SortingAlgorithmStressTest
│
├── /data
│   └── generated_data.csv       # Dataset (100,000 records)
│
├── /src
│   └── sorting_benchmark.py     # Core application and algorithms
│
└── README.md                    # Project documentation and benchmarks
````

---

## How to Run

1. **Preparation**
   Ensure `generated_data.csv` is located in the `/data` folder.

2. **Execution**
   Run the script from the project root:

   ```bash
   python src/sorting_benchmark.py
   ```

3. **Menu Options**

   * Select **Option 1** to run a custom test (algorithm, column, row count).
   * Select **Option 2** to execute the full benchmark suite shown above.
