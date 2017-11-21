class StableSelctionSort:
    def run(self, input_arr):
        length = len(input_arr)  # Take hold of the input_arr length

        for i in range(0, length - 1):  # iterate over the input_arr
            lowest_item_index = i  # assume lowest index is current index

            for j in range(i, length):  # iterate over the input_arr again from i to length on every i loop above
                if input_arr[j] < input_arr[lowest_item_index]:  # if the subsequent to i value is lower then one @ i
                    lowest_item_index = j  # lowest item index becomes the value at j

            key = input_arr[lowest_item_index]  # the value of the item at lowest_item_index
            while lowest_item_index > i:  # here we are moving the items to the right to free up some space
                input_arr[lowest_item_index] = input_arr[lowest_item_index - 1]
                lowest_item_index -= 1
            input_arr[i] = key  # we put the value of lowest_item_index into that spot in the array

        for item in input_arr:
            print item
