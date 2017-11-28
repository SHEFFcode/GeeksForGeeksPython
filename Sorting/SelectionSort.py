class SelectionSort:
    def run(self, input_arr):
        length = len(input_arr)

        for i in range(0, length - 1, 1):
            lowestItemIndex = i

            for j in range(i, length, 1):
                if input_arr[j] < input_arr[lowestItemIndex]:
                    lowestItemIndex = j

            if lowestItemIndex != i and input_arr[lowestItemIndex] != input_arr[i]:
                input_arr[lowestItemIndex], input_arr[i] = input_arr[i], input_arr[lowestItemIndex]  # actual swap

        for item in input_arr:
            print item
