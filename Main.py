class Main:
    from Sorting.MergeSort import MergeSort
    from Search.BinarySearch import BinarySearch
    from Search.InterpolationSearch import InterpolationSearch
    from Greedy.ActivitySelection import ActivitySelection

    activitySelection = ActivitySelection()
    activitySelection.run([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9])

    # interpolationSearch = InterpolationSearch()
    # print interpolationSearch.run_recursive([1, 2, 4, 6, 7, 10, 11, 14, 15], 0, 8, 4)
    # print interpolationSearch.run_iterative([1, 2, 4, 6, 7, 10, 11, 14, 15], 4)

    # binarySearch = BinarySearch()
    # binarySearch.run_recursive([0, 2, 3, 4, 10, 40, 44], 2, 0, 6)
    # binarySearch.run_iterative([0, 2, 3, 4, 10, 40, 44], 2)


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