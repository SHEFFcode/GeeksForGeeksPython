class BinarySearch:
    def run_recursive(self, input_arr, element, left, right):
        if left >= right:
            print("Element {0} is not in the input array".format(element))
        mid = left + (right - left) / 2
        if input_arr[mid] == element:
            print("Found element {0} at position {1}".format(element, mid + 1))
        elif input_arr[mid] > element:
            right = mid - 1  # because we do not want to consider the mid anymore
            self.run_recursive(input_arr, element, left, right)
        else:
            left = mid + 1  # because we do not want to consider the mid anymore
            self.run_recursive(input_arr, element, left, right)

    def run_iterative(self, input_arr, element):
        left = 0
        right = len(input_arr)

        while right >= left:
            mid = left + (right - left) / 2
            if input_arr[mid] == element:
                print("Found element {0} at position {1}".format(element, mid + 1))
            elif input_arr[mid] > element:
                right = mid - 1
            else:
                left = mid + 1
        if left >= right:  # we've reached the end of the while loop without finding the element
            print("{0} does not exist in this list".format(element))
