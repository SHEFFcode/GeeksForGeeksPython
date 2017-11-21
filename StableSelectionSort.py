class StableSelctionSort:
    def run(self, input_arr):
        length = len(input_arr)

        for i in range(0, length - 1, 1):
            lowest_item_index = i

            for j in range(i, length, 1):
                if input_arr[j] < input_arr[lowest_item_index]:
                    lowest_item_index = j

            key = input_arr[lowest_item_index]
            while lowest_item_index > i:
                input_arr[lowest_item_index] = input_arr[lowest_item_index - 1]
                lowest_item_index -= 1
            input_arr[i] = key

        for item in input_arr:
            print item


