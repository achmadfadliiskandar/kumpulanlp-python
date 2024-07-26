import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    elapsed_time = end_time - start_time

    return arr, elapsed_time

def selection_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    end_time = time.time()
    elapsed_time = end_time - start_time

    return arr, elapsed_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    end_time = time.time()
    elapsed_time = end_time - start_time

    return arr, elapsed_time

def main():
    # Input data numerik
    numeric_data = [64, 34, 25, 12, 22, 11, 90]

    # Input data string
    string_data = ["apple", "orange", "banana", "grape", "pineapple"]

    # Bubble Sort
    sorted_numeric, time_bubble_numeric = bubble_sort(numeric_data.copy())
    sorted_string, time_bubble_string = bubble_sort(string_data.copy())
    print("Bubble Sort (Numeric):", sorted_numeric)
    print("Time taken:", time_bubble_numeric, "seconds")
    print("Bubble Sort (String):", sorted_string)
    print("Time taken:", time_bubble_string, "seconds")

    print("\n" + "=" * 50 + "\n")

    # Selection Sort
    sorted_numeric, time_selection_numeric = selection_sort(numeric_data.copy())
    sorted_string, time_selection_string = selection_sort(string_data.copy())
    print("Selection Sort (Numeric):", sorted_numeric)
    print("Time taken:", time_selection_numeric, "seconds")
    print("Selection Sort (String):", sorted_string)
    print("Time taken:", time_selection_string, "seconds")

    print("\n" + "=" * 50 + "\n")

    # Insertion Sort
    sorted_numeric, time_insertion_numeric = insertion_sort(numeric_data.copy())
    sorted_string, time_insertion_string = insertion_sort(string_data.copy())
    print("Insertion Sort (Numeric):", sorted_numeric)
    print("Time taken:", time_insertion_numeric, "seconds")
    print("Insertion Sort (String):", sorted_string)
    print("Time taken:", time_insertion_string, "seconds")

if __name__ == "__main__":
    main()