📊 Sorting Algorithm Project
This project demonstrates the implementation of three different sorting algorithms: Heap Batch, Heap Increment, and Merge Sort. These algorithms were tested using datasets of varying sizes to evaluate their performance and efficiency.

✨ Features
Heap Batch Sorting: Implements batch heap sort to sort large datasets efficiently.
Heap Increment Sorting: A variant of heap sort where elements are incrementally added to the heap.
Merge Sort: A classic divide-and-conquer algorithm that splits and merges the dataset for efficient sorting.
Performance Testing: Each algorithm was tested with three datasets of different sizes to compare speed and efficiency.

📂 Datasets
The following datasets were used to test the performance of the sorting algorithms:

1000 Dataset.txt: Contains 1,000 data points.
10000 Dataset.txt: Contains 10,000 data points.
100000 Dataset.txt: Contains 100,000 data points.
These datasets were designed to simulate real-world scenarios where sorting efficiency can significantly impact performance.

🚀 How to Run
Clone or download the repository to your local machine.
Ensure that you have Python installed (or the programming language you used for the project).
Place the dataset files (1000 Dataset.txt, 10000 Dataset.txt, 100000 Dataset.txt) in the appropriate directory.
Run the sorting scripts for each algorithm.
For example, using Python, you would execute:

python test_heap.py

This script reads the dataset, applies the sorting algorithm, and outputs the sorted result along with performance metrics.

⚡ Performance Comparison
The three sorting algorithms were tested on the datasets to observe how they scale with increasing data sizes. Here's a general summary:

Heap Batch Sort: Efficient with larger datasets but may take more setup time for smaller datasets.
Heap Increment Sort: Handles incremental data additions well but may have slower performance compared to other methods for large datasets.
Merge Sort: Offers stable performance and is a good all-rounder for sorting, especially with larger datasets due to its predictable time complexity (O(n log n)).


📊 Results
After running the tests on the three datasets, the results showed how each algorithm performed in terms of execution time and memory usage. For detailed results and analysis, refer to the output logs in the project.
![image](https://github.com/user-attachments/assets/fe64344c-c47b-462b-8569-6c4f59e99531)


🎯 Why Did I Build This?
I built this project as an assignment for my Intro to Algorithms course during my master's program. It was a great way to apply the theoretical concepts I learned in class and get hands-on experience with different sorting techniques. The project helped me explore the performance of various algorithms and their efficiency with different dataset sizes.


💡 Future Improvements
Additional Sorting Algorithms: Implementing other algorithms like Quick Sort and Radix Sort for comparison.
Visualization: Adding visual representations of how the sorting algorithms work in real-time.
Parallel Processing: Experimenting with multi-threaded sorting to optimize performance for large datasets.

⚖️ License
This project is open-source and available for anyone to use, modify, or enhance. Feel free to contribute!

