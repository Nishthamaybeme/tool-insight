import matplotlib.pyplot as plt
import numpy as np

# Input sizes as powers of 10
input_sizes = [10**1, 10**2, 10**3, 10**4, 10**5]

# Execution times for each sorting algorithm in ms
bubble_sort_times = [0.0172, 0.2189, 7.0202, 187.6395, 22606.1111]
selection_sort_times = [0.0229, 0.1, 4.2967, 41.4216, 3220.8909]
insertion_sort_times = [0.0078, 0.0589, 3.0649, 68.6499, 3365.0207]
quick_sort_times = [0.016, 0.1412, 1.1504, 2.3155, 13.2844]
heap_sort_times = [0.0132, 0.1529, 0.5324, 3.0393, 28.0424]
merge_sort_times = [0.078, 0.1465, 2.228, 2.7521, 28.9273]
counting_sort_times = [0.0259, 0.0373, 0.2315, 0.8329, 3.2101]
radix_sort_times = [0.0145, 0.0627, 0.6645, 2.7048, 5.9484]

# Individual plots for all algorithms
def plot_algorithm_times(input_sizes, times, title, algorithm_name):
    plt.figure(figsize=(8, 5))
    plt.plot(input_sizes, times, marker='o', label=algorithm_name)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input Size (10^x)')
    plt.ylabel('Execution Time (ms)')
    plt.title(title)
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.legend()
    plt.show()

# Plotting individual algorithm performance
algorithms = [
    (bubble_sort_times, "Bubble Sort"),
    (selection_sort_times, "Selection Sort"),
    (insertion_sort_times, "Insertion Sort"),
    (quick_sort_times, "Quick Sort"),
    (heap_sort_times, "Heap Sort"),
    (merge_sort_times, "Merge Sort"),
    (counting_sort_times, "Counting Sort"),
    (radix_sort_times, "Radix Sort")
]

for times, name in algorithms:
    plot_algorithm_times(input_sizes, times, f"{name} Performance", name)

# Comparison plots by complexity category
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, bubble_sort_times, marker='o', label='Bubble Sort')
plt.plot(input_sizes, selection_sort_times, marker='o', label='Selection Sort')
plt.plot(input_sizes, insertion_sort_times, marker='o', label='Insertion Sort')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size (10^x)')
plt.ylabel('Execution Time (ms)')
plt.title('Comparison of O(n^2) Algorithms')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, quick_sort_times, marker='o', label='Quick Sort')
plt.plot(input_sizes, heap_sort_times, marker='o', label='Heap Sort')
plt.plot(input_sizes, merge_sort_times, marker='o', label='Merge Sort')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size (10^x)')
plt.ylabel('Execution Time (ms)')
plt.title('Comparison of O(n log n) Algorithms')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, counting_sort_times, marker='o', label='Counting Sort')
plt.plot(input_sizes, radix_sort_times, marker='o', label='Radix Sort')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size (10^x)')
plt.ylabel('Execution Time (ms)')
plt.title('Comparison of O(n) Algorithms')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.show()

# Comparison of all algorithms
plt.figure(figsize=(12, 8))
for times, name in algorithms:
    plt.plot(input_sizes, times, marker='o', label=name)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size (10^x)')
plt.ylabel('Execution Time (ms)')
plt.title('Comparison of All Sorting Algorithms')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.show()