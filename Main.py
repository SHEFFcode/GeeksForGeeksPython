class Main:
    from Sorting.MergeSort import MergeSort
    from Search.BinarySearch import BinarySearch

    binarySearch = BinarySearch()
    binarySearch.run_recursive([0, 2, 3, 4, 10, 40, 44], 2, 0, 6)
    binarySearch.run_iterative([0, 2, 3, 4, 10, 40, 44], 2)


    # mergeSort = MergeSort()
    # input_arr = [38, 27, 43, 3, 9, 82, 10]
    # mergeSort.run(input_arr, 0, len(input_arr) - 1)
    # for i in input_arr:
    #     print(i)


    # quickSort = Quicksort()
    # input_arr = [7, 2, 1, 6, 8, 5, 3, 4]
    # quickSort.quicksort_wrapper(input_arr, 0, len(input_arr) - 1)
    # for i in input_arr:
    #     print i

    # insertionSort = InsertionSort()
    # insertionSort.Run([23, 42, 4, 16, 8, 15])

    # selectionSort = SelectionSort()
    # selectionSort.Run([23, 42, 4, 16, 8, 15])
    #
    # stableSelectionSort = StableSelctionSort()
    # stableSelectionSort.Run([23, 42, 4, 16, 8, 15])