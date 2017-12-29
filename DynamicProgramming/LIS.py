class LIS:
    def run_lis(self, sequence_array, length):
        longest_increasing_subsequence = [0] * length
        max_increasing = 0
        for i in range(0, length):
            longest_increasing_subsequence[i] = 1
        for i in range(0, length):
            for j in range(0, i):
                if sequence_array[i] > sequence_array[j] and longest_increasing_subsequence[i] \
                        < longest_increasing_subsequence[j] + 1:
                    longest_increasing_subsequence[i] = longest_increasing_subsequence[j] + 1
        for i in range(0, length):
            if max_increasing < longest_increasing_subsequence[i]:
                max_increasing = longest_increasing_subsequence[i]
        return max_increasing
