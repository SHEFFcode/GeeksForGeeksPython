class MergeSort:
    def run(self, arr, l, r):
        if l < r:
            m = (l + r) / 2
            self.run(arr, l, m)
            self.run(arr, m + 1, r)
            self.merge(arr, l, m, r)

    @staticmethod
    def merge(arr, l, m, r):
        left_half_size = m - l + 1  # length of the left half (excluding mid)
        right_half_size = r - m  # length of right half (including mid)
        i, j = 0, 0  # iterator vars for later

        left_half = range(0, left_half_size)  # left half container
        right_half = range(0, right_half_size)  # right half container

        while i < left_half_size:  # fill in the left half from arr
            left_half[i] = arr[i + l]
            i += 1

        while j < right_half_size:  # fill in the right half from array
            right_half[j] = arr[j + m + 1]
            j += 1

        k = l  # keep track of left bound
        i, j = 0, 0  # reset iterator vars
        while i < left_half_size and j < right_half_size:  # while both left and right half pointers are in bounds (there are items to compare)
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < left_half_size:  # any remaining left half items
            arr[k] = left_half[i]
            i, k = i + 1, k + 1

        while j < right_half_size:
            arr[k] = right_half[j]  # any remaining right half items
            j, k = j + 1, k + 1
