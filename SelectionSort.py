class SelectionSort:
    def Run(self, inputArr):
        length = len(inputArr)

        for i in range(0, length - 1, 1):
            lowestItemIndex = i

            for j in range(i, length, 1):
                if inputArr[j] < inputArr[lowestItemIndex]:
                    lowestItemIndex = j

            if lowestItemIndex != i and inputArr[lowestItemIndex] != inputArr[i]:
                inputArr[lowestItemIndex], inputArr[i] = inputArr[i], inputArr[lowestItemIndex]  # actual swap

        for item in inputArr:
            print item


