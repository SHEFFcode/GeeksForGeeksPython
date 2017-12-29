class LPS:
    def run_lps(self, sequence):
        length = len(sequence)
        container = [[0 for x in range(0, length)] for y in range(0, length)]
        for i in range(0, length):
            container[i][i] = 1
        for cl in range(2, length + 1):
            for i in range(0, length - cl + 1):
                j = i + cl - 1
                if sequence[i] == sequence[j] and cl == 2:
                    container[i][j] = 2
                elif sequence[i] == sequence[j]:
                    container[i][j] = container[i + 1][j - 1] + 2
                else:
                    container[i][j] = max(container[i][j - 1], container[i + 1][j])
        return container[0][length - 1]
