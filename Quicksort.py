class Quicksort:
    def quicksort_wrapper(self, a, start, end):
        if start < end:
            partition_index = self.partition(a, start, end)
            self.quicksort_wrapper(a, start, partition_index - 1)
            self.quicksort_wrapper(a, partition_index + 1, end)

    @staticmethod
    def partition(a, start, end):
        pivot = a[end]
        i = start - 1
        for j in range(start, end, 1):
            if a[j] < pivot:
                i += 1
                a[j], a[i] = a[i], a[j]

        a[i + 1], a[end] = a[end], a[i + 1]

        return i + 1