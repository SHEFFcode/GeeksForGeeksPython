class MergeSort:
    def run(self, arr, l, r):
        if l < r:
            m = (l + r) / 2
            self.run(arr, l, m)
            self.run(arr, m + 1, r)
            self.merge(arr, l, m, r)

    @staticmethod
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        i, j = 0, 0

        L = range(0, n1)
        R = range(0, n2)

        while i < n1:
            L[i] = arr[l + i]
            i += 1

        while j < n2:
            R[j] = arr[m + 1 + j]
            j += 1

        k = l
        i, j = 0, 0
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
