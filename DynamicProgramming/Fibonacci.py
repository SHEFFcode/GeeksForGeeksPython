class Fibonacci:
    def run_recursive(self, desired_fib):
        return desired_fib if desired_fib == 0 or desired_fib == 1 else self.run_recursive(desired_fib - 1) \
                                                                        + self.run_recursive(desired_fib - 2)

    def run_memoization(self, desired_fib, memoization_array=None):
        if memoization_array is None:
            memoization_array = [-1] * (desired_fib + 1)
        if desired_fib == 0 or desired_fib == 1:
            return desired_fib
        if memoization_array[desired_fib] != -1:
            return memoization_array[desired_fib]
        else:
            memoization_array[desired_fib] = self.run_memoization(desired_fib - 1, memoization_array) \
                                             + self.run_memoization(desired_fib - 2, memoization_array)
            return memoization_array[desired_fib]

    @staticmethod
    def run_tabulation(desired_fib, tabulation_array=None):
        if tabulation_array is None:
            tabulation_array = [-1] * (desired_fib + 1)
            tabulation_array[0] = 0
            tabulation_array[1] = 1
        for i in range(2, desired_fib + 1):
            tabulation_array[i] = tabulation_array[i - 1] + tabulation_array[i - 2]
        return tabulation_array[desired_fib]