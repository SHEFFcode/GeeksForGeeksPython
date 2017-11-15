class StableSelctionSort:
    def Run(self, inputArr):
        length = len(inputArr)

        for i in range(0, length - 1, 1):
            lowestItemIndex = i

            for j in range(i, length, 1):
                if inputArr[j] < inputArr[lowestItemIndex]:
                    lowestItemIndex = j

            key = inputArr[lowestItemIndex]
            while lowestItemIndex > i:
                inputArr[lowestItemIndex] = inputArr[lowestItemIndex - 1]
                lowestItemIndex -= 1
            inputArr[i] = key

        for item in inputArr:
            print item


