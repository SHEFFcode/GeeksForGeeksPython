class Main:
    from SelectionSort import SelectionSort
    from StableSelectionSort import StableSelctionSort

    selectionSort = SelectionSort()
    selectionSort.Run([23, 42, 4, 16, 8, 15])

    stableSelectionSort = StableSelctionSort()
    stableSelectionSort.Run([23, 42, 4, 16, 8, 15])