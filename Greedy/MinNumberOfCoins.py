class MinNumberOfCoins:
    def run(self, denominations_array, change_to_give):
        coins_used = []

        for i in range(len(denominations_array) - 1, -1, -1):  # we want to start from the highest denomination possible
            while change_to_give >= denominations_array[i] and change_to_give > 0:  # we go from back to front while change is bigger
                change_to_give -= denominations_array[i]  # update the amount of change we still need to give
                coins_used.append(denominations_array[i])  # append the coins used to the purse

        for coin in coins_used:  # we are just gonna print out the result here after we are done iterating
            print(coin)
