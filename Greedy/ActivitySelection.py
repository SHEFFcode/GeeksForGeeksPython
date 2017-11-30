class ActivitySelection:
    def run(self, start_array, end_array):
        i = 0  # first activity always gets selected
        print(i)

        for j in range(1, len(start_array)):
            if start_array[j] >= end_array[i]:  # the start time of the next activity is after end of curr activity
                print(j)
                i = j  # set curr activity to next activity
