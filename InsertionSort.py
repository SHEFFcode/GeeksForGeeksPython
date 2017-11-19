class InsertionSort:
    def run(self, input_arr):
        length = len(input_arr)
        for i in range(0, length, 1):
            key = input_arr[i]
            j = i - 1
            while j >= 0 and key < input_arr[j]:
                input_arr[j + 1] = input_arr[j]
                j -= 1

            input_arr[j + 1] = key

        for item in input_arr:
            print item