from heap import *
from merge import *
import matplotlib.pyplot as plt
import time

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

if __name__ == "__main__":
    files = ["1000 Dataset.txt", "10000 Dataset.txt", "100000 Dataset.txt"]

    batch_times = []
    incre_times = []
    merge_times = []

    for file in files:
        a_file = open(file)
        names, ratings = [], []
        next(a_file)
        name_score_dict = {}
        for line in a_file:
            temp = line.rstrip().split('; ')
            names.append(temp[0])  # key: name
            ratings.append(float(temp[1]))  # name: rating
            name_score_dict[temp[0]] = float(temp[1])

        _, time_batch = measure_time(sort_movies_batch, names.copy(), ratings.copy(), name_score_dict)
        _, time_incre = measure_time(sort_movies_incre, names.copy(), ratings.copy(), name_score_dict)
        _, time_merge = measure_time(merge_sort, ratings.copy())

        print(f"Runtime for {file}:")
        print(f"Heap Batch Sorting: {time_batch} seconds")
        print(f"Heap Incremental Sorting: {time_incre} seconds")
        print(f"Merge Sorting: {time_merge} seconds")

        batch_times.append(time_batch)
        incre_times.append(time_incre)
        merge_times.append(time_merge)

    # Plotting
    plt.figure(figsize=(10, 6))
    bar_width = 0.25
    index = range(len(files))

    plt.bar(index, batch_times, width=bar_width, color='blue', label='Heap Batch Sorting')
    plt.bar([i + bar_width for i in index], incre_times, width=bar_width, color='green', label='Heap Incremental Sorting')
    plt.bar([i + 2 * bar_width for i in index], merge_times, width=bar_width, color='orange', label='Merge Sorting')

    # Adding labels and title
    plt.xlabel('File')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithm Comparison')
    plt.xticks([i + bar_width/2 for i in index], files)
    plt.legend()
    plt.show()
