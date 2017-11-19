class StableSelctionSort:
    def run(self, input_arr):
        length = len(input_arr)

        for i in range(0, length - 1, 1):
            lowestItemIndex = i

            for j in range(i, length, 1):
                if input_arr[j] < input_arr[lowestItemIndex]:
                    lowestItemIndex = j

            key = input_arr[lowestItemIndex]
            while lowestItemIndex > i:
                input_arr[lowestItemIndex] = input_arr[lowestItemIndex - 1]
                lowestItemIndex -= 1
            input_arr[i] = key

        for item in input_arr:
            print item


