import datetime

class MinNumberOfPlatforms:
    @staticmethod
    def run(arrival_array, departure_array):
        arrival_array.sort()
        departure_array.sort()
        n = len(arrival_array)  # does not matter which array, as they will have same # of elements
        max_platforms, result, i, j = 1, 1, 1, 0  # we set max platforms, result and i to 1, since we need at least 1

        while i < n and j < n:  # basically just an iterator loop
            if arrival_array[i] < departure_array[j]:  # we have a train arriving before prev train has departed
                max_platforms, i = max_platforms + 1, i + 1  # we will need to have at least one more platform
                if max_platforms > result:  # We have the number of platforms being larger then it's been so far
                    result = max_platforms
            else:  # we ran out of items, or we have a departure before another arrival
                max_platforms, j = max_platforms - 1, j + 1

        print("You need to have {0} platforms for this schedule".format(result))
        return result
