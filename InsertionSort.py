class InsertionSort:
    def Run(self, inputArr):
        length = len(inputArr)
        for i in range(0, length, 1):
            key = inputArr[i]
            j = i - 1
            while j >= 0 and key < inputArr[j]:
                inputArr[j + 1] = inputArr[j]
                j -= 1

            inputArr[j + 1] = key

        for item in inputArr:
            print item