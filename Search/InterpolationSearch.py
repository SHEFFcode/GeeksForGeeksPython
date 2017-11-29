class InterpolationSearch:
    def run_iterative(self, input_arr, element):
        start, end, pos = 0, len(input_arr) - 1, 0

        while start <= end and input_arr[start] <= element <= input_arr[end]:  # while start <= end and el is in bounds
            pos = self._get_position(input_arr, start, end, element)
            if input_arr[pos] == element:
                return pos
            elif input_arr[pos] < element:
                start = pos + 1
            else:
                end = pos - 1
        return -1  # we did not find the element

    def run_recursive(self, input_arr, start, end, element):
        if start > end:
            return -1  # we did not find the element
        pos = self._get_position(input_arr, start, end, element)
        if input_arr[pos] == element:
            return pos
        elif input_arr[pos] < element:
            return self.run_recursive(input_arr, pos + 1, end, element)
        else:
            return self.run_recursive(input_arr, start, pos - 1, element)

    @staticmethod
    def _get_position(input_arr, start, end, element):
        return start + ((end - start) / (input_arr[end] - input_arr[start])) * (element - input_arr[start])
