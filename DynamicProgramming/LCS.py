class LCS:
    @staticmethod
    def run_lcs(string_one, string_two, len_one, len_two):
        container = [[0 for x in range(len_two + 1)] for y in range(len_one + 1)]
        for i in range(0, len_one + 1):
            for j in range(0, len_two + 1):
                if i == 0 or j == 0:
                    container[i][j] = 0
                elif string_one[i - 1] == string_two[j - 1]:
                    container[i][j] = container[i - 1][j - 1] + 1
                else:
                    container[i][j] = max(container[i - 1][j], container[i][j - 1])
        return container[len_one][len_two]
