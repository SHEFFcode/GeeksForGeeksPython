class MergeSort:
    def run(self, arr, l, r):
        if l < r:
            m = (l + r) / 2
            self.run(arr, l, m)
            self.run(arr, m + 1, r)
            self.merge(arr, l, m, r)

    @staticmethod
    def merge(arr, l, m, r):
        n1 = m - 1 + 1
        n2 = r - m

        L = [None] * n1
        R = [None] * n2

        for i in range(0, n1, 1):
            L[i] = arr[l + 1]
        for j in range(0, n2, 1):
            R[j] = arr[m + 1 + j]

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

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
