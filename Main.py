class Main:
    from Sorting.MergeSort import MergeSort
    from Search.BinarySearch import BinarySearch
    from Search.InterpolationSearch import InterpolationSearch
    from Greedy.ActivitySelection import ActivitySelection
    from Greedy.MinNumberOfPlatforms import MinNumberOfPlatforms
    import datetime
    from Greedy.MinNumberOfCoins import MinNumberOfCoins
    from Greedy.DijkstrasShortestPath import DijkstrasShortestPath
    from DynamicProgramming import TravelingSalesman
    from DynamicProgramming import LCS
    from DynamicProgramming import LIS
    from DynamicProgramming import  LPS
    from DynamicProgramming import Fibonacci
    from Greedy import WWP

    wwp = WWP.WWP()
    wwp.run_wwp("aaa bb cc dddd")

    # fibonacci = Fibonacci.Fibonacci()
    # print(fibonacci.run_recursive(6))
    # print(fibonacci.run_memoization(6))
    # print(fibonacci.run_tabulation(6))


    # lps = LPS.LPS()
    # print(lps.run_lps("BBABCBCAB"))

    # lis = LIS.LIS()
    # print(lis.run_lis([10, 22, 9, 33, 21, 50, 41, 60], 8))

    # lcs = LCS.LCS()
    # print(lcs.run_lcs("AGGTAB", "GTXTXAYB", 6, 8))

    # traveling_salesman = TravelingSalesman.TravelingSalesman()
    # graph = [
    #     [0, 1, 15, 6],
    #     [2, 0, 7, 3],
    #     [9, 6, 0, 12],
    #     [10, 4, 8, 0]
    # ]
    # traveling_salesman.calculate_cost(graph)

    # ditkas_shortest_path = DijkstrasShortestPath()
    # graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2],
    #          [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0],
    #          [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    # ditkas_shortest_path.run(graph, 0)

    # min_number_of_coins = MinNumberOfCoins()
    # min_number_of_coins.run([1, 2, 5, 10, 20, 50, 100], 121)

    # min_number_of_platforms = MinNumberOfPlatforms()
    # min_number_of_platforms.run([datetime.time(9, 0), datetime.time(9, 40), datetime.time(9, 50), datetime.time(11, 00),
    #                             datetime.time(18, 00)],
    #                             [datetime.time(9, 10), datetime.time(12, 00), datetime.time(11, 20),
    #                             datetime.time(11, 30), datetime.time(19, 00), datetime.time(20, 00)]
    #                             )

    # activitySelection = ActivitySelection()
    # activitySelection.run([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9])

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